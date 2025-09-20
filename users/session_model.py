from pydantic import BaseModel
from datetime import datetime

class Session(BaseModel):
  user_id: str
  gym_id: str
  name: str | None
  start_time: datetime
  end_time: datetime | None
  duration_minutes: int | None
  notes: str | None
  mood_rating: int | None
  energy_rating: int | None


class SessionCreate(BaseModel):
  user_id: str
  gym_id: str
  name: str | None
  start_time: datetime


class SessionUpdate(BaseModel):
  name: str | None
  notes: str | None
  mood_rating: int | None
  energy_rating: int | None