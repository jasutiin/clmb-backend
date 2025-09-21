from fastapi import FastAPI
from endpoints import gyms, gym_routes

app = FastAPI()

app.include_router(gyms.router)
app.include_router(gym_routes.router)