from study_agent.prompts import build_summary_prompt, build_tasks_prompt


def test_build_summary_prompt_contains_content():
    prompt = build_summary_prompt("Python loops")
    assert "Python loops" in prompt


def test_build_summary_prompt_instructs_summarize():
    prompt = build_summary_prompt("test content")
    assert "Summarize" in prompt or "summarize" in prompt


def test_build_tasks_prompt_contains_content():
    prompt = build_tasks_prompt("Python loops")
    assert "Python loops" in prompt


def test_build_tasks_prompt_instructs_tasks():
    prompt = build_tasks_prompt("test content")
    assert "task" in prompt.lower()
