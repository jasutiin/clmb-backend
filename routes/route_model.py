from pydantic import BaseModel
from datetime import datetime

class GradeSystem(BaseModel):
    id: str
    name: str # v-scale, font scale, or any custom scale a gym may have
    description: str | None
    country_origin: str | None


class Grade(BaseModel):
    id: str
    grade_system_id: str
    value: str 

    """
    this property makes it easier to query grades.
    e.g. we want to find all grades that are harder than V5,
    just do difficulty > 4 (0-indexed)
    """
    difficulty_order: int

    description: str | None
    created_at: datetime


class Route(BaseModel):
    gym_id: str
    name: str | None
    grade: Grade
    color: str | None
    setter_name: str | None
    wall_section: str | None
    route_type: str 
    difficulty_rating: int | None
    is_active: bool
    date_set: datetime | None 
    date_removed: datetime | None
    description: str | None