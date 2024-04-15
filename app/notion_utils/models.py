from pydantic import BaseModel


class Text(BaseModel):
    content: str = ""
    link: str | None = None


class RichText(BaseModel):
    type: str = "text"
    text: Text = Text()


class Code(BaseModel):
    caption: list[RichText] = []
    rich_text: list[RichText] = []
    language: str = ""


class CodeBlock(BaseModel):
    code: Code
    type: str = "code"


class Todo(BaseModel):
    rich_text: list[RichText] = []
    checked: bool = False
    color: str = "blue"
    children: list = []


class TodoBlock(BaseModel):
    to_do: Todo
    type: str = "to_do"


class BulletedListItem(BaseModel):
    rich_text: list[RichText] = []
    color: str = "default"
    children: list = []


class BulletedListItemBlock(BaseModel):
    bulleted_list_item: BulletedListItem
    type: str = "bulleted_list_item"


class NumberedListItem(BaseModel):
    rich_text: list[RichText] = []
    color: str = "default"
    children: list = []


class NumberedListItemBlock(BaseModel):
    numbered_list_item: NumberedListItem
    type: str = "numbered_list_item"
