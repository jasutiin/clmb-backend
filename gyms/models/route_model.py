from pydantic import BaseModel
from datetime import datetime

class GradeSystem(BaseModel):
  id: str
  name: str # v-scale, font scale, or any custom scale a gym may have
  description: str | None
  created_at: datetime
  modified_at: datetime


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

  created_at: datetime
  modified_at: datetime


class Route(BaseModel):
  id: str
  gym: str
  grade: str
  name: str | None
  colour: str | None
  section: str | None
  created_at: datetime
  modified_at: datetime