import pytest
from httpx import AsyncClient


async def test_add(client: AsyncClient):
    task = {
        "title": "string",
        "description": "string",
        "status": "todo"
    }
    response = await client.post("/tasks", json=task)
    body = response.json()
    assert response.status_code == 200
    assert body['detail'] == "Задача успешно добавлена!"


@pytest.mark.usefixtures("create_task")
async def test_get(client: AsyncClient):
    response = await client.get("/tasks/10")
    body = response.json()
    assert response.status_code == 200
    assert body['data'] == {"task_id": 10,
                            "title": "string",
                            "description": "string",
                            "status": "todo"}


async def test_get_failed(client: AsyncClient):
    response = await client.get("/tasks/101")
    body = response.json()
    assert response.status_code == 404
    assert body['detail'] == "Задача не найдена!"
