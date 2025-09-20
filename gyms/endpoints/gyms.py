from main import app
from fastapi import Query
from typing import Optional

@app.get("/gyms/{gym_id}")
async def get_gym(gym_id: str):
  """
  GET the details of a single gym.
  
  :param gym_id: The Id of the gym passed in as a route parameter.
  """
  pass


@app.get("/gyms")
async def get_gyms(
  city: Optional[str] = Query(None),
  country: Optional[str] = Query(None),
  limit: int = Query(20, ge=1, le=100)
):
  """
  GET all gyms with optional filtering.
  
  :param city: Filter gyms by city
  :param country: Filter gyms by country
  :param limit: Number of gyms to return
  """
  pass