from learning_sprint_planner_agent.agent import agent
from learning_sprint_planner_agent.chains.explain import explain_chain
from learning_sprint_planner_agent.data.course_catalogue import COURSE_CATALOGUE
from learning_sprint_planner_agent.schemas import StudyRequest


def get_course_from_catalogue(
    topic: str,
    level: str,
) -> dict:
    """Retrieve course details from the local course catalogue."""

    topic = topic.strip().lower()
    level = level.strip().lower()

    for catalogue_topic, levels in COURSE_CATALOGUE.items():
        if catalogue_topic.lower() == topic:
            for catalogue_level, details in levels.items():
                if catalogue_level.lower() == level:
                    return details

    raise ValueError(
        f"No course found for topic '{topic}' at level '{level}'."
    )


def validate_study_request(
    request: StudyRequest,
    total_hours: float,
) -> None:
    """Validate study request against the course's total hours."""

    if request.completed_hours > total_hours:
        raise ValueError(
            "Completed hours cannot be greater than total course hours."
        )


def run_explain(
    topic: str,
    level: str,
) -> str:
    """Generate an explanation for a learning topic."""

    return explain_chain.invoke(
        {
            "topic": topic,
            "level": level,
        }
    )


def run_plan(
    request: StudyRequest,
) -> dict:
    """Generate a learning plan using the ReAct agent."""

    course = get_course_from_catalogue(
        request.topic,
        request.level,
    )

    validate_study_request(
        request,
        course["total_hours"],
    )

    result = agent.invoke(
        {
            "messages": [
                {
                    "role": "user",
                    "content": (
                        f"I want to learn {request.level} {request.topic}. "
                        f"I have completed {request.completed_hours} hours "
                        f"and can study {request.hours_per_day} hours per day."
                    ),
                }
            ]
        }
    )

    return result