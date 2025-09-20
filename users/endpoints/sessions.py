from main import app
from users.models.session_model import Session, SessionCreate, SessionUpdate
from users.models.climb_model import Climb

@app.get("/users/{user_id}/sessions")
async def get_sessions(user_id: str):
  """
  GET all sessions of a user.

  :param user_id: The Id of the user passed in as a route parameter.
  """

  pass


@app.get("/sessions/{session_id}")
async def get_session(session_id: str):
  """
  GET the details of a single session. This includes all climbs of that session.

  :param session_id: The Id of the particular session passed in as another route parameter.
  """
    
  pass


@app.post("/sessions", response_model=Session)
async def create_session(session: SessionCreate):
  """
  CREATE a new climbing session.
  
  :param session: Session data in request body
  """
  pass


@app.put("/sessions/{session_id}", response_model=Session)
async def update_session(session_id: str, session_update: SessionUpdate):
  """
  UPDATE an existing session (edit notes, ratings, etc.).
  
  :param session_id: The Id of the session to update
  :param session_update: Updated session data
  """
  pass


@app.patch("/sessions/{session_id}/end")
async def end_session(session_id: str):
  """
  END a session (set end_time and calculate duration).
  
  :param session_id: The Id of the session to end
  """
  pass