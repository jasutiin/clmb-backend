from main import app

@app.get("/users/{user_id}")
async def get_user(user_id: str):
  """
  GET the profile of a user.

  :param user_id: The Id of the user passed in as a route parameter.
  """
  
  pass