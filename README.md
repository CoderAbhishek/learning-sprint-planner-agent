# 🎓 Learning Sprint Planner Agent

An AI-powered learning planner built with **Python, LangChain, Groq, Pydantic, and Streamlit**.

The application helps learners either **generate a structured learning plan** or **get an explanation of a learning topic** based on their selected topic, difficulty level, completed study hours, and available study time.

The project combines **deterministic Python logic** for validation, calculations, and course data with an **LLM-powered ReAct agent** for reasoning and natural-language planning.

---

## Overview

Learning plans often require combining structured information with reasoning.

For example, given:

* Topic: Advanced Python
* Level: Advanced
* Completed hours: 10
* Available study time: 2 hours/day

the application can determine the course requirements, calculate the remaining study hours, calculate the required number of study days, and generate a structured learning plan.

The application deliberately separates deterministic responsibilities from LLM responsibilities:

* **Python** handles validation, calculations, and authoritative course data.
* **LangChain tools** expose deterministic capabilities to the agent.
* **The ReAct agent** handles tool selection and planning.
* **Groq** provides the underlying chat model.
* **Streamlit** provides the user interface.

---

## Key Features

### 📚 Learning Plan Generation

Generate a structured learning plan using:

* Topic
* Difficulty level
* Completed study hours
* Available study hours per day

The planning workflow uses a LangChain ReAct agent with custom tools.

### 💡 Topic Explanation

Explain a learning topic for a selected learner level using an LCEL chain.

The explanation flow uses:

```text
ChatPromptTemplate
        ↓
Chat Model
        ↓
StrOutputParser
```

### 🗂️ Local Course Catalogue

The application uses a controlled local course catalogue containing:

* Python
* SQL
* Generative AI
* LangChain
* Machine Learning

Each topic contains Beginner, Intermediate, and Advanced course information where applicable, including total hours and prerequisites.

### 🛡️ Deterministic Validation

Business rules are enforced outside the LLM.

For example:

```text
Completed hours > Total course hours
```

is rejected before the ReAct agent is invoked.

### 🧰 Custom LangChain Tools

The agent has access to three tools:

* `get_course_details`
* `calculate_remaining_hours`
* `calculate_completion_days`

### 🧪 Automated Testing

The project includes a pytest test suite covering:

* Pydantic validation
* Course catalogue lookup
* Calculation tools
* Edge cases
* Explain-mode application logic
* Plan-mode validation
* Agent interface behaviour

Current test suite:

```text
21 tests passed
```

---

## Architecture

```text
                         ┌─────────────────────┐
                         │    Streamlit UI     │
                         └──────────┬──────────┘
                                    │
                                    ▼
                         ┌─────────────────────┐
                         │   application.py    │
                         │   Application Layer │
                         └──────────┬──────────┘
                                    │
                    ┌───────────────┴───────────────┐
                    │                               │
                    ▼                               ▼
            ┌───────────────┐              ┌─────────────────┐
            │ Explain Mode  │              │   Plan Mode     │
            └───────┬───────┘              └────────┬────────┘
                    │                               │
                    ▼                               ▼
             ┌─────────────┐              ┌─────────────────┐
             │  LCEL Chain │              │ Pydantic +      │
             │             │              │ Deterministic   │
             │ Prompt      │              │ Validation      │
             │     ↓       │              └────────┬────────┘
             │ Chat Model  │                       │
             │     ↓       │                       ▼
             │ Parser      │              ┌─────────────────┐
             └──────┬──────┘              │  ReAct Agent    │
                    │                     └────────┬────────┘
                    ▼                              │
             ┌─────────────┐                       ▼
             │    Groq     │              ┌─────────────────┐
             │ Chat Model  │              │ Custom Tools    │
             └─────────────┘              │                 │
                                          │ Course Details   │
                                          │ Remaining Hours  │
                                          │ Completion Days  │
                                          └─────────────────┘
```

---

## How It Works

### Plan Mode

The planning workflow follows this sequence:

```text
User Input
    ↓
Pydantic StudyRequest
    ↓
Course Catalogue Lookup
    ↓
Business Validation
    ↓
ReAct Agent
    ↓
Tool Selection
    ↓
Tool Execution
    ↓
LLM Reasoning
    ↓
Learning Plan
```

The agent can use the available tools to:

1. Retrieve course details.
2. Calculate remaining study hours.
3. Calculate the required number of study days.
4. Generate the final learning plan.

### Explain Mode

Explain mode uses a simpler LCEL pipeline:

```text
User Input
    ↓
ChatPromptTemplate
    ↓
Groq Chat Model
    ↓
StrOutputParser
    ↓
Explanation
```

The explanation flow does not require the ReAct agent because it does not need tool-based planning.

---

## Tools

### `get_course_details`

Retrieves course information from the local course catalogue.

```text
Input:
    topic
    level

Output:
    total_hours
    prerequisites
```

The catalogue is treated as the authoritative source for course-specific information.

Unknown topics are not automatically invented by the application.

---

### `calculate_remaining_hours`

Calculates:

```text
remaining hours = total hours - completed hours
```

The tool rejects completed hours greater than the total course hours.

---

### `calculate_completion_days`

Calculates:

```text
completion days = ceil(remaining hours / hours per day)
```

The calculation uses `math.ceil()` so that a partial study day is counted as a complete required day.

---

## Validation & Error Handling

Validation is intentionally separated into different layers.

### Pydantic

`StudyRequest` validates the structure and basic constraints of user input.

```text
topic             → non-empty string
level             → non-empty string
completed_hours   → >= 0
hours_per_day     → > 0
```

### Application Layer

The application layer validates course-specific business rules.

For example:

```text
completed_hours <= course total hours
```

### Tool Layer

Individual tools also validate their own numerical contracts.

This creates a clear separation:

```text
Pydantic
    ↓
Input structure

Application layer
    ↓
Business rules

Tools
    ↓
Calculation contracts

LLM
    ↓
Reasoning and natural-language generation
```

This prevents critical deterministic rules from depending solely on LLM behaviour.

---

## Tech Stack

| Technology            | Purpose                                  |
| --------------------- | ---------------------------------------- |
| Python                | Application development                  |
| LangChain             | LLM orchestration and tools              |
| LangChain LCEL        | Explain-mode chain                       |
| LangChain ReAct Agent | Learning-plan orchestration              |
| Groq                  | LLM inference                            |
| Pydantic              | Input validation                         |
| Streamlit             | Web interface                            |
| pytest                | Automated testing                        |
| uv                    | Python project and dependency management |

---

## Project Structure

```text
learning-sprint-planner-agent/
│
├── src/
│   └── learning_sprint_planner_agent/
│       ├── agent.py
│       ├── application.py
│       ├── config.py
│       ├── schemas.py
│       ├── tools.py
│       │
│       ├── chains/
│       │   ├── __init__.py
│       │   └── explain.py
│       │
│       ├── data/
│       │   └── course_catalogue.py
│       │
│       └── models/
│           ├── __init__.py
│           └── groq.py
│
├── tests/
│   ├── test_agent.py
│   ├── test_chain.py
│   ├── test_schemas.py
│   └── test_tools.py
│
├── .env.example
├── .gitignore
├── pyproject.toml
├── streamlit_app.py
├── uv.lock
└── README.md
```

---

## Installation

### Prerequisites

Make sure the following are installed:

* Python
* uv
* Git

### Clone the repository

```bash
git clone <your-repository-url>
cd learning-sprint-planner-agent
```

### Install dependencies

```bash
uv sync
```

### Configure environment variables

Create a `.env` file from `.env.example`.

```env
GROQ_API_KEY=your_groq_api_key
GROQ_MODEL=openai/gpt-oss-20b
```

Do not commit `.env` to the repository.

---

## Running the Application

Launch the Streamlit application with:

```bash
uv run streamlit run streamlit_app.py
```

The application provides two modes:

### Plan

Generate a structured learning plan based on:

* Topic
* Level
* Completed hours
* Study hours per day

### Explain

Generate an explanation of the selected topic for the chosen learner level.

---

## Running Tests

Run the complete test suite:

```bash
uv run pytest
```

The current test suite contains:

```text
21 tests
```

The tests are designed to avoid unnecessary external API calls.

For example, the Explain chain and agent interfaces are tested using test doubles rather than making live Groq requests.

---

## Testing Strategy

The project separates deterministic unit tests from model-dependent behaviour.

### Unit Tests

The following are tested deterministically:

* Pydantic validation
* Course lookup
* Calculation logic
* Invalid input handling
* Application orchestration
* Chain interface
* Agent interface

### Model Behaviour

The actual Groq model is used during application execution rather than being required for every unit test.

This makes the test suite:

* Faster
* More deterministic
* Less expensive
* Independent of temporary API/network issues

---

## Design Decisions

### Why a local course catalogue?

The initial version uses controlled application data rather than external search.

This keeps course-specific information deterministic and prevents the model from inventing catalogue information.

### Why ReAct?

The planning workflow involves selecting and combining multiple tools.

The ReAct agent provides the orchestration required to:

```text
Reason
  ↓
Select Tool
  ↓
Execute Tool
  ↓
Observe Result
  ↓
Continue Reasoning
```

### Why LCEL for Explain mode?

Explain mode does not require iterative tool use.

A simple:

```text
Prompt → Model → Parser
```

pipeline is therefore sufficient.

### Why keep validation outside the LLM?

Validation and numerical calculations are deterministic responsibilities.

The LLM is used for:

* Reasoning
* Tool selection
* Natural-language generation
* Structuring the final response

Python is used for:

* Validation
* Course data
* Arithmetic
* Business rules

---

## Current Limitations

The current version intentionally keeps the scope focused.

It does not currently include:

* RAG
* Vector databases
* External course search
* Web search
* Long-term memory
* User accounts
* Persistent databases
* FastAPI
* LangGraph implementation
* Production deployment infrastructure

The course catalogue is currently maintained as local application data.

---

## Future Improvements

Potential future extensions include:

* Expanding the course catalogue
* Adding more sophisticated learning-plan generation
* Adding progress tracking
* Persisting learner history
* Integrating external course resources
* Adding retrieval capabilities
* Adding richer Streamlit visualisations
* Adding evaluation for generated learning plans
* Adding production deployment

---

## Project Philosophy

The project follows a simple principle:

> **Use deterministic code where correctness matters, and use the LLM where reasoning and natural-language generation add value.**

This keeps the system easier to understand, test, debug, and extend while still demonstrating practical LangChain agent development.

---

## License

This project is intended as a learning and portfolio project.
