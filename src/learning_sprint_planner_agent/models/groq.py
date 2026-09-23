"""Groq chat-model construction for the application."""

from langchain_groq import ChatGroq

from learning_sprint_planner_agent.config import GROQ_MODEL


def create_groq_chat_model() -> ChatGroq:
    """Create the Groq chat model used by this application."""
    return ChatGroq(
        model=GROQ_MODEL,
        temperature=0,
        max_tokens=300,
        timeout=30,
        max_retries=2,
    )