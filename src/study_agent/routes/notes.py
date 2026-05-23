from fastapi import APIRouter, Depends, HTTPException

from study_agent import repository
from study_agent.database import get_connection
from study_agent.schemas import NoteCreate, NoteResponse, NoteUpdate

router = APIRouter()


def get_db():
    from study_agent.config import DATABASE_PATH

    conn = get_connection(DATABASE_PATH)
    try:
        yield conn
    finally:
        conn.close()


@router.get("/", response_model=list[NoteResponse])
async def list_notes(db=Depends(get_db)):
    return repository.select_all_notes(db)


@router.post("/", response_model=NoteResponse, status_code=201)
async def create_note(note: NoteCreate, db=Depends(get_db)):
    return repository.insert_note(db, note.title, note.content)


@router.get("/{note_id}", response_model=NoteResponse)
async def get_note(note_id: int, db=Depends(get_db)):
    result = repository.select_note_by_id(db, note_id)
    if result is None:
        raise HTTPException(status_code=404, detail="Note not found")
    return result


@router.put("/{note_id}", response_model=NoteResponse)
async def update_note(note_id: int, note: NoteUpdate, db=Depends(get_db)):
    result = repository.update_note(db, note_id, note.title, note.content)
    if result is None:
        raise HTTPException(status_code=404, detail="Note not found")
    return result


@router.delete("/{note_id}", status_code=204)
async def delete_note(note_id: int, db=Depends(get_db)):
    deleted = repository.delete_note(db, note_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Note not found")
