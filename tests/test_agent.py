import pytest

from learning_sprint_planner_agent import application
from learning_sprint_planner_agent.schemas import StudyRequest


def test_run_plan_rejects_completed_hours_above_course_total(
    monkeypatch,
):
    request = StudyRequest(
        topic="Python",
        level="Advanced",
        completed_hours=60,
        hours_per_day=2,
    )

    def fake_agent_invoke(_):
        raise AssertionError(
            "The agent should not be called for invalid input."
        )

    monkeypatch.setattr(
        application.agent,
        "invoke",
        fake_agent_invoke,
    )

    with pytest.raises(
        ValueError,
        match="Completed hours cannot be greater than total course hours.",
    ):
        application.run_plan(request)


def test_get_course_from_catalogue_returns_correct_course():
    result = application.get_course_from_catalogue(
        "Python",
        "Advanced",
    )

    assert result["total_hours"] == 50
    assert result["prerequisites"] == ["Intermediate Python"]


def test_get_course_from_catalogue_is_case_insensitive():
    result = application.get_course_from_catalogue(
        "python",
        "advanced",
    )

    assert result["total_hours"] == 50


def test_get_course_from_catalogue_rejects_unknown_course():
    with pytest.raises(
        ValueError,
        match="No course found",
    ):
        application.get_course_from_catalogue(
            "Java",
            "Beginner",
        )


def test_run_plan_passes_valid_request_to_agent(monkeypatch):
    request = StudyRequest(
        topic="Python",
        level="Advanced",
        completed_hours=10,
        hours_per_day=2,
    )

    def fake_agent_invoke(input_data):
        assert input_data == {
            "messages": [
                {
                    "role": "user",
                    "content": (
                        "I want to learn Advanced Python. "
                        "I have completed 10.0 hours "
                        "and can study 2.0 hours per day."
                    ),
                }
            ]
        }

        return {
            "messages": [
                {
                    "role": "assistant",
                    "content": "Mock learning plan",
                }
            ]
        }

    monkeypatch.setattr(
        application.agent,
        "invoke",
        fake_agent_invoke,
    )

    result = application.run_plan(request)

    assert result["messages"][-1]["content"] == "Mock learning plan"