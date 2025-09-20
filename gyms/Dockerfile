FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# for documentation, doesn't actually do anything
EXPOSE 8002

# without --host flag, it defaults to local host which is not what docker uses inside the container
# localhost: 127.0.0.1, docker0: 172.17.0.1 (according to google)
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8002"]