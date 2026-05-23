from fastapi import FastAPI

from study_agent.routes import notes, web

app = FastAPI(title="Study Agent")
app.include_router(web.router)
app.include_router(notes.router, prefix="/api/notes", tags=["notes"])


@app.get("/health")
async def health():
    return {"status": "ok"}
