from langchain.agents import create_agent

from learning_sprint_planner_agent.models.groq import create_groq_chat_model
from learning_sprint_planner_agent.tools import (
    get_course_details,
    calculate_remaining_hours,
    calculate_completion_days,
)


model = create_groq_chat_model()

agent = create_agent(
    model=model,
    tools=[
        get_course_details,
        calculate_remaining_hours,
        calculate_completion_days,
    ],
    system_prompt=(
        "You are a Learning Sprint Planner. "
        "Help users plan their learning using the available course catalogue. "
        "Course information must come from the get_course_details tool. "
        "Never invent course information for courses that are not in the catalogue."
    ),
)


if __name__ == "__main__":
    result = agent.invoke(
        {
            "messages": [
                {
                    "role": "user",
                    "content": (
                        "I want to learn Advanced Python. "
                        "I have already completed 10 hours and "
                        "can study 2 hours per day. "
                        "How many days will I need?"
                    ),
                }
            ]
        }
    )

    print(result)