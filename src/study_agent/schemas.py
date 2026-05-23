from datetime import datetime

from pydantic import BaseModel


class NoteCreate(BaseModel):
    title: str
    content: str


class NoteResponse(BaseModel):
    id: int
    title: str
    content: str
    summary: str | None = None
    tasks: str | None = None
    created_at: datetime

    model_config = {"from_attributes": True}
