from pydantic import BaseModel

class User(BaseModel):
  email: str
  username: str
  first_name: str | None
  last_name: str | None
  display_name: str | None
  bio: str | None
  avatar_url: str | None

  preferred_climbing_style: str | None
  current_boulder_grade: str | None
  current_rope_grade: str | None
  years_climbing: int | None
  climbing_goals: str | None
  home_gym_id: str | None

  preferred_units: str
  timezone: str | None
  privacy_level: str

  city: str | None
  state: str | None
  country: str | None

  is_verified: bool
  is_premium: bool