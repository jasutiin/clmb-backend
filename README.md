# clmb-backend

This is the backend for clmb, an app to keep track of all your climbs!

### Tech Stack

- Python
- FastAPI
- PostgreSQL
- Docker
- Kubernetes

### Architecture

This project will be using a microservices architecture.

### Setup

1. Go to each folder representing a microservice and create a virtual environment: `py -m venv .venv`.
2. Using separate terminals for each microservice, start their virtual environments: `.venv/Scripts/activate`.
3. To run each microservice, do
   `uvicorn main:app`. Must have separate terminals for each microservice.
