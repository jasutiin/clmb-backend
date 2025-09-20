FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# for documentation, doesn't actually do anything
EXPOSE 8002

CMD [ "python", "main.py" ]