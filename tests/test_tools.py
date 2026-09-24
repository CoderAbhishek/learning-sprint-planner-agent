import pytest

from learning_sprint_planner_agent.tools import (
    calculate_completion_days,
    calculate_remaining_hours,
    get_course_details,
)


def test_get_course_details_returns_python_advanced_course():
    result = get_course_details.invoke(
        {
            "topic": "Python",
            "level": "Advanced",
        }
    )

    assert result["total_hours"] == 50
    assert result["prerequisites"] == ["Intermediate Python"]


def test_get_course_details_is_case_insensitive():
    result = get_course_details.invoke(
        {
            "topic": "python",
            "level": "advanced",
        }
    )

    assert result["total_hours"] == 50


def test_get_course_details_returns_error_for_unknown_course():
    result = get_course_details.invoke(
        {
            "topic": "Java",
            "level": "Beginner",
        }
    )

    assert "error" in result


def test_calculate_remaining_hours():
    result = calculate_remaining_hours.invoke(
        {
            "total_hours": 50,
            "completed_hours": 10,
        }
    )

    assert result == 40


def test_calculate_remaining_hours_rejects_invalid_completed_hours():
    with pytest.raises(ValueError):
        calculate_remaining_hours.invoke(
            {
                "total_hours": 50,
                "completed_hours": 60,
            }
        )


def test_calculate_completion_days():
    result = calculate_completion_days.invoke(
        {
            "remaining_hours": 40,
            "hours_per_day": 2,
        }
    )

    assert result == 20


def test_calculate_completion_days_rounds_up():
    result = calculate_completion_days.invoke(
        {
            "remaining_hours": 41,
            "hours_per_day": 2,
        }
    )

    assert result == 21


def test_calculate_completion_days_rejects_negative_remaining_hours():
    with pytest.raises(ValueError):
        calculate_completion_days.invoke(
            {
                "remaining_hours": -5,
                "hours_per_day": 2,
            }
        )


def test_calculate_completion_days_rejects_zero_hours_per_day():
    with pytest.raises(ValueError):
        calculate_completion_days.invoke(
            {
                "remaining_hours": 40,
                "hours_per_day": 0,
            }
        )