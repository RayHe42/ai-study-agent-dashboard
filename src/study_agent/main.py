from contextlib import asynccontextmanager
from pathlib import Path

from fastapi import FastAPI
from fastapi.templating import Jinja2Templates

from study_agent.config import TEMPLATES_DIR
from study_agent.database import init_db
from study_agent.routes import notes, web

templates = Jinja2Templates(directory=str(TEMPLATES_DIR))


@asynccontextmanager
async def lifespan(app: FastAPI):
    init_db()
    yield


app = FastAPI(title="Study Agent", lifespan=lifespan)
app.include_router(web.router)
app.include_router(notes.router, prefix="/api/notes", tags=["notes"])


@app.get("/health")
async def health():
    return {"status": "ok"}
