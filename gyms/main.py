from fastapi import FastAPI
from gym_model import Gym

app = FastAPI()

@app.get("/gyms/{gym_id}")
async def get_gym(gym_id):
  return {"gym_id": gym_id}


@app.post("/gyms")
async def add_gym(gym: Gym):
  return gym


@app.get("/gyms/{gym_id}/routes")
async def get_routes(route_id):
  return {"gym_id": gym_id}


@app.get("/gyms/{gym_id}/routes/{route_id}")
async def get_route(route_id):
  return {"route_id": route_id}


@app.post("/gyms/{gym_id}/routes")
async def add_route(gym: Route):
  return gym