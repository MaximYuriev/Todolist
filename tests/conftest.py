import pytest
from httpx import AsyncClient, ASGITransport
from sqlalchemy import NullPool
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker

from config import POSTGRES_USER, POSTGRES_PASSWORD, POSTGRES_HOST, POSTGRES_PORT, POSTGRES_TEST_DB
from db import Base, get_session
from src.main import app

db_url_test = f"postgresql+asyncpg://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_TEST_DB}"

test_db_engine = create_async_engine(db_url_test, echo=False, poolclass=NullPool)
test_async_session = async_sessionmaker(test_db_engine, expire_on_commit=False)


async def override_get_session():
    async with test_async_session() as session:
        yield session


app.dependency_overrides[get_session] = override_get_session


@pytest.fixture(autouse=True, scope='session')
async def prepare_db():
    async with test_db_engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield
    async with test_db_engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)


@pytest.fixture(scope="session")
async def client():
    async with AsyncClient(transport=ASGITransport(app=app), base_url="http://test") as client:
        yield client
