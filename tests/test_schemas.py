import pytest
from pydantic import ValidationError

from learning_sprint_planner_agent.schemas import StudyRequest


def test_valid_study_request():
    request = StudyRequest(
        topic="Python",
        level="Advanced",
        completed_hours=10,
        hours_per_day=2,
    )

    assert request.topic == "Python"
    assert request.level == "Advanced"
    assert request.completed_hours == 10
    assert request.hours_per_day == 2


def test_empty_topic_is_invalid():
    with pytest.raises(ValidationError):
        StudyRequest(
            topic="",
            level="Beginner",
            completed_hours=0,
            hours_per_day=2,
        )


def test_empty_level_is_invalid():
    with pytest.raises(ValidationError):
        StudyRequest(
            topic="Python",
            level="",
            completed_hours=0,
            hours_per_day=2,
        )


def test_negative_completed_hours_is_invalid():
    with pytest.raises(ValidationError):
        StudyRequest(
            topic="Python",
            level="Beginner",
            completed_hours=-1,
            hours_per_day=2,
        )


def test_zero_hours_per_day_is_invalid():
    with pytest.raises(ValidationError):
        StudyRequest(
            topic="Python",
            level="Beginner",
            completed_hours=0,
            hours_per_day=0,
        )


def test_negative_hours_per_day_is_invalid():
    with pytest.raises(ValidationError):
        StudyRequest(
            topic="Python",
            level="Beginner",
            completed_hours=0,
            hours_per_day=-2,
        )