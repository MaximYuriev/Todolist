FROM python:3.11

RUN mkdir /app
WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

CMD alembic upgrade head
CMD uvicorn src.main:app --reload --workers 1 --host 0.0.0.0 --port 8000