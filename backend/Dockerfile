FROM python:3.11-slim

RUN apt-get update && apt-get install -y postgresql-client && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY requirements.txt .
COPY start.sh .
RUN pip install --no-cache-dir -r requirements.txt

COPY ./app /app/app

CMD ["./start.sh"]
