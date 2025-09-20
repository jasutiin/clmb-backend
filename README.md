# clmb-backend

This is the backend for clmb, an app to keep track of all your climbs!

### Tech Stack

- Python
- FastAPI
- PostgreSQL
- Docker
- Kubernetes

### Architecture

<img width="581" height="396" alt="clmb microservice drawio" src="https://github.com/user-attachments/assets/fab96357-e228-40d7-8a19-c9a8b83250e7" />

This is the overall microservices architecture that I will be implementing. The idea is to have a Kubernetes (K8s) cluster that manages the creation and deletion of pods within each microservice. This makes the backend scalable. If for whatever reason the Users microservice was put under a lot of load, and all the other microservices had less load, then Kubernetes would create another pod within that Users microservice so that it would be faster.

Each microservice has its own dedicated storage. This is called the [Database-per-service pattern](https://docs.aws.amazon.com/prescriptive-guidance/latest/modernization-data-persistence/database-per-service.html). This makes it so that all the microservices are loosely coupled from each other. You may have noticed that each storage is external from the Kubernetes cluster. This is because pods inside a K8s cluster are ephemeral in nature, meaning that they last a short amount of time. They are added and removed frequently. This interferes with the stateful nature of a database where data must persist independently of any specific pod's lifecycle. If a database's data were stored directly within a pod, that data would be lost forever when the pod is terminated, restarted, or rescheduled, making the database unusable and unreliable.

The API Gateway inside of the cluster is responsible for building responses to send back to the client. This is called the [API composition pattern](https://docs.aws.amazon.com/prescriptive-guidance/latest/modernization-data-persistence/api-composition.html). Let's say the client wanted to get the information of some user, their sessions, and the gym that those sessions were held in. Without the API Gateway, the client would have to make two separate REST API requests to the backend. The API Gateway is responsible for taking REST API requests from the user, and calling the microservices necessary to complete the request.

As of now, I am planning on using REST as the communication protocol between microservices. The plan is to use gRPC later on, but my main focus is to learn Kubernetes and Docker so best not to add too many new technologies.<br><br>

<img width="1188" alt="clmb database drawio" src="https://github.com/user-attachments/assets/4c358ab3-9826-472e-a1e3-714ec4a9b031" />

This is the database schema. Still need to add some more things, but for now this is sufficient for an MVP.<br><br>

<img width="555" height="591" alt="clmb interaction drawio" src="https://github.com/user-attachments/assets/56af94be-a71b-4d68-b1b0-2e8337cdc84c" />

This is how I understand the interaction flow of the application to be like.

### Setup

1. Go to each folder representing a microservice and create a virtual environment: `py -m venv .venv`.
2. Using separate terminals for each microservice, start their virtual environments: `.venv/Scripts/activate`.
3. To run each microservice, do
   `uvicorn main:app`. Must have separate terminals for each microservice.
