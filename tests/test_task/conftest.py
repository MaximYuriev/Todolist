import pytest

from repositories.task import TaskRepository
from tests.conftest import test_async_session

@pytest.fixture()
async def task_repository():
    async with test_async_session() as session:
        yield TaskRepository(session)

@pytest.fixture()
async def create_task(task_repository):
    task_data = {
        "task_id": 10,
        "title": "string",
        "description": "string",
        "status": "todo"
    }
    await task_repository.add(task_data)