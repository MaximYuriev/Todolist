import os

from dotenv import load_dotenv

load_dotenv()

POSTGRES_USER=os.environ.get("POSTGRES_USER")
POSTGRES_PASSWORD=os.environ.get("POSTGRES_PASSWORD")
POSTGRES_HOST=os.environ.get("POSTGRES_HOST")
POSTGRES_PORT=os.environ.get("POSTGRES_PORT")
POSTGRES_DB=os.environ.get("POSTGRES_DB")

POSTGRES_TEST_DB=os.environ.get("POSTGRES_TEST_DB")