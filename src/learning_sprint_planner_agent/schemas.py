from pydantic import BaseModel, Field


class StudyRequest(BaseModel):
    topic: str = Field(min_length=1)
    level: str = Field(min_length=1)
    completed_hours: float = Field(ge=0)
    hours_per_day: float = Field(gt=0)