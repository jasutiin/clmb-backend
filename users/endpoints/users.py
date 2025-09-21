from fastapi import APIRouter

router = APIRouter()

@router.get("/users/{user_id}")
async def get_user(user_id: str):
  """
  GET the profile of a user.

  :param user_id: The Id of the user passed in as a route parameter.
  """
  
  return {"text": "hello"}