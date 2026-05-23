from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker

from study_agent.config import DATABASE_URL

engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(bind=engine)


class Base(DeclarativeBase):
    pass


def init_db():
    """Create all tables defined by ORM models that inherit from Base."""
    import study_agent.models  # noqa: F401 — ensure models are registered

    Base.metadata.create_all(bind=engine)


def get_db():
    """FastAPI dependency that yields a DB session and closes it after use."""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
