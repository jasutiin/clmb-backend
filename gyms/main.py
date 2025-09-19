from fastapi import FastAPI
from gym_model import Gym

app = FastAPI()

@app.get("/gyms/{gym_id}")
async def get_gym(gym_id):
  return {"gym_id": gym_id}


@app.post("/gyms")
async def add_gym(gym: Gym):
  return gym