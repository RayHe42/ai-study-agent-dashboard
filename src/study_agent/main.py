from contextlib import asynccontextmanager

from fastapi import FastAPI

from study_agent.config import DATABASE_PATH
from study_agent.database import init_db
from study_agent.routes import notes, web


@asynccontextmanager
async def lifespan(app: FastAPI):
    init_db(DATABASE_PATH)
    yield


app = FastAPI(title="Study Agent", lifespan=lifespan)
app.include_router(web.router)
app.include_router(notes.router, prefix="/api/notes", tags=["notes"])


@app.get("/health")
async def health():
    return {"status": "ok"}
