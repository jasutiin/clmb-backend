from pydantic import BaseModel
from datetime import datetime
from decimal import Decimal

class Gym(BaseModel):
  id: str
  grade_system_id: str
  name: str
  slug: str
  address: str | None
  city: str | None
  country: str | None
  latitude: Decimal | None
  longitude: Decimal | None
  phone: str | None
  email: str | None
  website: str | None
  description: str | None
  created_at: datetime
  modified_at: datetime