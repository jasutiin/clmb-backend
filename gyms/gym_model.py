from pydantic import BaseModel

class Gym(BaseModel):
  name: str
  slug: str

  address: str
  city: str
  country: str
  latitude: int
  longitude: int

  phone: str | None
  email: str | None
  website: str | None
  description: str | None