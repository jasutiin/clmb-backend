from fastapi import FastAPI
from endpoints import users, sessions

app = FastAPI()

app.include_router(users.router)
app.include_router(sessions.router)