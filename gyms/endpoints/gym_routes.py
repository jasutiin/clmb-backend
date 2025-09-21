from fastapi import APIRouter, Query
from typing import Optional

router = APIRouter()

@router.get("/gyms/{gym_id}/routes")
async def get_gym_routes(
  gym_id: str,
  grade: Optional[str] = Query(None),
  section: Optional[str] = Query(None),
  is_active: bool = Query(True)
):
  """
  GET all routes for a specific gym.
  
  :param gym_id: The Id of the gym
  :param grade: Filter by specific grade
  :param section: Filter by wall section
  :param is_active: Only return active routes
  """
  return {"text": "hello"}


@router.get("/routes/{route_id}")
async def get_route(route_id: str):
  """
  GET the details of a single route.
  
  :param route_id: The Id of the route return passed in as a route parameter.
  """
  return {"text": "hello"}