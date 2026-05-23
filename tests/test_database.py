from sqlalchemy import inspect

from study_agent.database import Base, engine, init_db


def test_init_db_creates_notes_table():
    # Drop all tables first so we test creation from scratch
    Base.metadata.drop_all(bind=engine)
    init_db()

    inspector = inspect(engine)
    tables = inspector.get_table_names()
    assert "notes" in tables


def test_notes_table_has_expected_columns():
    init_db()
    inspector = inspect(engine)
    columns = {col["name"] for col in inspector.get_columns("notes")}
    assert "id" in columns
    assert "title" in columns
    assert "content" in columns
    assert "summary" in columns
    assert "tasks" in columns
