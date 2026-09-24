import math

from langchain_core.tools import tool

from learning_sprint_planner_agent.data.course_catalogue import COURSE_CATALOGUE


@tool
def get_course_details(topic: str, level: str) -> dict:
    """Retrieve course details for a topic and difficulty level."""

    topic = topic.strip().lower()
    level = level.strip().lower()

    for catalogue_topic, levels in COURSE_CATALOGUE.items():
        if catalogue_topic.lower() == topic:
            for catalogue_level, details in levels.items():
                if catalogue_level.lower() == level:
                    return details

    return {
        "error": f"No course found for topic '{topic}' at level '{level}'."
    }


@tool
def calculate_remaining_hours(
    total_hours: float,
    completed_hours: float,
) -> float:
    """Calculate the remaining study hours from total and completed hours."""

    if completed_hours > total_hours:
        raise ValueError(
            "Completed hours cannot be greater than total course hours."
        )

    return total_hours - completed_hours


@tool
def calculate_completion_days(
    remaining_hours: float,
    hours_per_day: float,
) -> int:
    """Calculate the number of study days needed to complete the remaining hours."""

    if remaining_hours < 0:
        raise ValueError("Remaining hours cannot be negative.")

    if hours_per_day <= 0:
        raise ValueError("Hours per day must be greater than zero.")

    return math.ceil(remaining_hours / hours_per_day)