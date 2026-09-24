COURSE_CATALOGUE = {
    "Python": {
        "Beginner": {
            "total_hours": 20,
            "prerequisites": [],
        },
        "Intermediate": {
            "total_hours": 35,
            "prerequisites": ["Python basics"],
        },
        "Advanced": {
            "total_hours": 50,
            "prerequisites": ["Intermediate Python"],
        },
    },
    "SQL": {
        "Beginner": {
            "total_hours": 15,
            "prerequisites": [],
        },
        "Intermediate": {
            "total_hours": 25,
            "prerequisites": ["SQL basics"],
        },
        "Advanced": {
            "total_hours": 40,
            "prerequisites": ["Intermediate SQL"],
        },
    },
    "Generative AI": {
        "Beginner": {
            "total_hours": 25,
            "prerequisites": ["Python basics"],
        },
        "Intermediate": {
            "total_hours": 40,
            "prerequisites": ["Generative AI basics"],
        },
        "Advanced": {
            "total_hours": 60,
            "prerequisites": ["Intermediate Generative AI"],
        },
    },
    "LangChain": {
        "Beginner": {
            "total_hours": 20,
            "prerequisites": ["Python basics", "LLM fundamentals"],
        },
        "Intermediate": {
            "total_hours": 35,
            "prerequisites": ["LangChain basics"],
        },
        "Advanced": {
            "total_hours": 50,
            "prerequisites": ["Intermediate LangChain"],
        },
    },
    "Machine Learning": {
        "Beginner": {
            "total_hours": 30,
            "prerequisites": ["Python basics"],
        },
        "Intermediate": {
            "total_hours": 50,
            "prerequisites": ["Machine Learning basics"],
        },
        "Advanced": {
            "total_hours": 75,
            "prerequisites": ["Intermediate Machine Learning"],
        },
    },
}