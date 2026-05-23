from fastapi import APIRouter

router = APIRouter()


@router.get("/")
async def list_notes():
    return {"notes": []}


@router.post("/")
async def create_note():
    return {"message": "not implemented"}


@router.get("/{note_id}")
async def get_note(note_id: int):
    return {"note_id": note_id}


@router.post("/{note_id}/summarize")
async def summarize_note(note_id: int):
    return {"note_id": note_id, "summary": "[mock]"}


@router.post("/{note_id}/tasks")
async def generate_tasks(note_id: int):
    return {"note_id": note_id, "tasks": ["[mock task]"]}
