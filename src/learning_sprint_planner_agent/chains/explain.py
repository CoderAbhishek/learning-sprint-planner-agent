from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate

from learning_sprint_planner_agent.models.groq import create_groq_chat_model


prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            (
                "You are a helpful learning advisor. "
                "Explain learning concepts clearly and practically. "
                "Keep explanations concise but useful."
            ),
        ),
        (
            "human",
            (
                "Explain the following learning topic for a {level} learner:\n\n"
                "{topic}"
            ),
        ),
    ]
)


model = create_groq_chat_model()

parser = StrOutputParser()

explain_chain = prompt | model | parser

if __name__ == "__main__":
    result = explain_chain.invoke(
        {
            "topic": "Python generators",
            "level": "Beginner",
        }
    )

    print(result)