from pydantic import BaseModel, Field


class StudyRequest(BaseModel):
    topic: str = Field(min_length=1)
    duration_days: int = Field(gt=0)
    hours_per_day: float = Field(gt=0)
    level: str