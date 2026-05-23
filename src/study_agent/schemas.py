from datetime import datetime

from pydantic import BaseModel


class NoteCreate(BaseModel):
    title: str
    content: str


class NoteRead(BaseModel):
    id: int
    title: str
    content: str
    summary: str | None
    tasks: str | None
    created_at: datetime

    model_config = {"from_attributes": True}
