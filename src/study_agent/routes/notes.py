from datetime import datetime, timezone

from fastapi import APIRouter, HTTPException

from study_agent.schemas import NoteCreate, NoteResponse

router = APIRouter()

_notes_db: list[dict] = []
_next_id: int = 1


@router.get("/", response_model=list[NoteResponse])
async def list_notes():
    return _notes_db


@router.post("/", response_model=NoteResponse, status_code=201)
async def create_note(note: NoteCreate):
    global _next_id
    new_note = {
        "id": _next_id,
        "title": note.title,
        "content": note.content,
        "summary": None,
        "tasks": None,
        "created_at": datetime.now(timezone.utc),
    }
    _notes_db.append(new_note)
    _next_id += 1
    return new_note


@router.get("/{note_id}", response_model=NoteResponse)
async def get_note(note_id: int):
    for note in _notes_db:
        if note["id"] == note_id:
            return note
    raise HTTPException(status_code=404, detail="Note not found")
