from pydantic import BaseModel
from datetime import datetime

class Climb(BaseModel):
  route_id: str
  session_id: str | None
  attempt_type: str
  success: bool
  attempts: int
  rating: int | None
  notes: str | None
  climbed_at: datetime
    
  route_grade: str | None
  route_name: str | None
  gym_name: str | None