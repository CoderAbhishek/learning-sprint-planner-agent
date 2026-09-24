import streamlit as st

from learning_sprint_planner_agent.application import run_explain, run_plan
from learning_sprint_planner_agent.data.course_catalogue import COURSE_CATALOGUE
from learning_sprint_planner_agent.schemas import StudyRequest


st.set_page_config(
    page_title="Learning Sprint Planner",
    page_icon="🎓",
    layout="wide",
)


# -------------------------------------------------------------------
# Header
# -------------------------------------------------------------------

st.title("🎓 Learning Sprint Planner")
st.caption(
    "Build a structured learning plan or get a clear explanation of a topic."
)


# -------------------------------------------------------------------
# Sidebar
# -------------------------------------------------------------------

with st.sidebar:
    st.header("Learning Setup")

    mode = st.radio(
        "Mode",
        ["Plan", "Explain"],
    )

    topic = st.selectbox(
        "Topic",
        list(COURSE_CATALOGUE.keys()),
    )

    level = st.selectbox(
        "Level",
        ["Beginner", "Intermediate", "Advanced"],
    )


# -------------------------------------------------------------------
# Plan Mode
# -------------------------------------------------------------------

if mode == "Plan":
    st.subheader("Create Your Learning Plan")
    st.write(
        "Tell us how much you have already completed and how much "
        "time you can study each day."
    )

    col1, col2 = st.columns(2)

    with col1:
        completed_hours = st.number_input(
            "Completed hours",
            min_value=0.0,
            value=0.0,
            step=0.5,
        )

    with col2:
        hours_per_day = st.number_input(
            "Study hours per day",
            min_value=0.5,
            value=2.0,
            step=0.5,
        )

    st.divider()

    if st.button(
        "🚀 Generate Learning Plan",
        type="primary",
        use_container_width=True,
    ):
        try:
            request = StudyRequest(
                topic=topic,
                level=level,
                completed_hours=completed_hours,
                hours_per_day=hours_per_day,
            )

            with st.spinner("Creating your learning plan..."):
                result = run_plan(request)

            final_response = result["messages"][-1].content

            st.success("Learning plan generated successfully.")

            st.subheader("Your Learning Plan")
            st.markdown(final_response)

        except ValueError as error:
            st.error(str(error))

        except Exception:
            st.error(
                "Something went wrong while generating the learning plan. "
                "Please try again."
            )


# -------------------------------------------------------------------
# Explain Mode
# -------------------------------------------------------------------

else:
    st.subheader("Explain a Learning Topic")
    st.write(
        "Get a practical explanation tailored to your selected "
        "learner level."
    )

    st.info(
        f"Explaining **{topic}** for an **{level}** learner."
    )

    if st.button(
        "💡 Explain Topic",
        type="primary",
        use_container_width=True,
    ):
        try:
            with st.spinner("Preparing explanation..."):
                response = run_explain(topic, level)

            st.success("Explanation generated successfully.")

            st.subheader("Explanation")
            st.markdown(response)

        except Exception:
            st.error(
                "Something went wrong while generating the explanation. "
                "Please try again."
            )


# -------------------------------------------------------------------
# Footer
# -------------------------------------------------------------------

st.divider()

st.caption(
    "Built with Python • LangChain • Groq • Pydantic • Streamlit"
)