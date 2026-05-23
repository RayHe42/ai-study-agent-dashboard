import sqlite3

from study_agent.database import get_connection, init_db


def test_init_db_creates_notes_table(tmp_path):
    db_path = str(tmp_path / "test.db")
    init_db(db_path)

    conn = sqlite3.connect(db_path)
    rows = conn.execute(
        "SELECT name FROM sqlite_master WHERE type='table' AND name='notes'"
    ).fetchall()
    conn.close()
    assert len(rows) == 1


def test_init_db_is_idempotent(tmp_path):
    db_path = str(tmp_path / "test.db")
    init_db(db_path)
    init_db(db_path)  # should not raise

    conn = sqlite3.connect(db_path)
    rows = conn.execute(
        "SELECT name FROM sqlite_master WHERE type='table' AND name='notes'"
    ).fetchall()
    conn.close()
    assert len(rows) == 1


def test_notes_table_has_expected_columns(tmp_path):
    db_path = str(tmp_path / "test.db")
    init_db(db_path)

    conn = get_connection(db_path)
    columns = {row["name"] for row in conn.execute("PRAGMA table_info(notes)")}
    conn.close()
    assert "id" in columns
    assert "title" in columns
    assert "content" in columns
    assert "summary" in columns
    assert "tasks" in columns
    assert "created_at" in columns
    assert "updated_at" in columns
