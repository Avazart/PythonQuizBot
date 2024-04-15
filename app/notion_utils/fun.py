from .models import (
    Code,
    CodeBlock,
    NumberedListItem,
    NumberedListItemBlock,
    RichText,
    Text,
    Todo,
    TodoBlock,
)


def make_todo_block(
    text: str,
    checked: bool = False,
    color: str = "default",
) -> dict:
    block = TodoBlock(
        to_do=Todo(
            rich_text=[RichText(text=Text(content=text))],
            checked=checked,
            color=color,
        )
    )
    return block.model_dump()


def make_n_list_item(
    text: str,
    color: str = "default",
    children: list | None = None,
) -> dict:
    block = NumberedListItemBlock(
        numbered_list_item=NumberedListItem(
            rich_text=[RichText(text=Text(content=text))],
            color=color,
            children=children or [],
        )
    )
    return block.model_dump()


def make_code_block(
    text: str,
    language: str,
    captions: list[str] | None = None,
) -> dict:
    captions = captions or []
    block = CodeBlock(
        code=Code(
            caption=[
                RichText(text=Text(content=caption_text))
                for caption_text in captions
            ],
            rich_text=[RichText(text=Text(content=text))],
            language=language,
        )
    )
    return block.model_dump()
