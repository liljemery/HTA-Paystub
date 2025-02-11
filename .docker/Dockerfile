FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt /app/

RUN pip install --no-cache-dir -r requirements.txt

COPY . /app

CMD ["fastapi", "run", "main.py", "--port", "8000", "--host", "0.0.0.0"]
