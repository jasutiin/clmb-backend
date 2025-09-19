from fastapi import FastAPI
from route_model import Route

app = FastAPI()

@app.get("/gyms/{gym_id}/routes")
async def get_gym(gym_id):
  return {"gym_id": gym_id}


@app.get("/gyms/{gym_id}/routes/{route_id}")
async def get_gym(route_id):
  return {"route_id": route_id}


@app.post("/gyms/{gym_id}/routes")
async def add_gym(gym: Route):
  return gym