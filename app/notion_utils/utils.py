import logging
from datetime import datetime
from pathlib import Path

from notion_client import Client

from ..database.models import Option, Question, Quiz
from ..quiz_parser import from_file
from .fun import make_code_block, make_n_list_item, make_todo_block

logger = logging.getLogger(__name__)


def parse_page_id(source: str) -> str | None:
    if source.startswith("https://www.notion.so"):
        return source.rsplit("-", maxsplit=1)[1]
    return None


def export_to_notion(quiz_path: Path, parent_id: str, client: Client) -> str:
    quiz = from_file(quiz_path, quiz_path.name, quiz_path.stem)

    children = []
    for q in quiz.questions:
        item_children = []
        if q.code:
            item_children.append(make_code_block(q.code, language="python"))
        for option in q.options:
            item_children.append(make_todo_block(option.text, option.correct))
        children.append(make_n_list_item(q.text, children=item_children))

    parent = {"page_id": parent_id}
    properties = {
        "title": [{"text": {"content": quiz.name}}],
    }
    r = client.pages.create(
        parent=parent,
        children=children,
        properties=properties,
    )
    return r["url"]  # type: ignore


def _get_text(n_list_item) -> str:
    return n_list_item["rich_text"][0]["plain_text"]


def _get_code(children: list) -> str | None:
    for child in children:
        if code := child.get("code"):
            return _get_text(code)
    return None


def _get_todo_list(children: list) -> list[tuple[str, bool]]:
    items = []
    for child in children:
        if to_do := child.get("to_do"):
            text = _get_text(to_do)
            checked = to_do["checked"]
            items.append((text, checked))
    return items


def _get_page_title(response):
    return response["properties"]["title"]["title"][0]["text"]["content"]


def _get_last_edited_time(response) -> datetime:
    return datetime.fromisoformat(response["last_edited_time"]).replace(
        tzinfo=None
    )


def import_from_notion(page_id: str, source: str, client: Client) -> Quiz:
    response = client.pages.retrieve(page_id=page_id)
    title = _get_page_title(response)
    last_edited_time = _get_last_edited_time(response)

    page_children = client.blocks.children.list(block_id=page_id)
    questions = []
    q_n = 1
    for block in page_children["results"]:  # type: ignore
        if n_list_item := block.get("numbered_list_item"):
            block_id = block["id"]
            text = _get_text(n_list_item)
            block_children = client.blocks.children.list(block_id=block_id)

            code = _get_code(block_children["results"])  # type: ignore
            list_of_options = _get_todo_list(block_children["results"])  # type: ignore
            if not list_of_options:
                logger.warning("Missed list of options, skiped")
                continue

            options = [
                Option(n=n, text=text, correct=correct)
                for n, (text, correct) in enumerate(list_of_options)
            ]
            q = Question(text=text, code=code, n=q_n, options=options)
            questions.append(q)
            q_n += 1
    return Quiz(
        source=source,
        name=title,
        last_modified=last_edited_time,
        questions=questions,
    )
