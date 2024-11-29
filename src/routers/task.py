from typing import Annotated

from fastapi import APIRouter, Depends

from src.models.task import Task
from src.schemas.task import TaskCreate, TaskUpdate
from src.services.task import TaskService
from src.utils.dependencies import get_task_by_id
from src.utils.status import StatusEnum

task_router = APIRouter(prefix="/tasks", tags=["Task"])


@task_router.post("")
async def add_task(
        task: TaskCreate,
        task_service: Annotated[TaskService, Depends(TaskService)]
):
    await task_service.add_task(task)
    return {"detail": "Задача успешно добавлена!", "data": None}


@task_router.get("")
async def get_tasks(
        task_service: Annotated[TaskService, Depends(TaskService)],
        status: StatusEnum | None = None
):
    tasks = await task_service.get_all_tasks(status)
    return {"detail": "Найденные задачи:", "data": tasks}


@task_router.get("/{task_id}")
async def get_task(task: Annotated[Task, Depends(get_task_by_id)]):
    return {"detail": "Найденная задача:", "data": task}


@task_router.put("/{task_id}")
async def update_task(
        task: Annotated[Task, Depends(get_task_by_id)],
        task_update: TaskUpdate,
        task_service: Annotated[TaskService, Depends(TaskService)]
):
    await task_service.update_task(task, task_update)
    return {"detail": "Задача успешно изменена!", "data": None}

@task_router.delete("/{task_id}")
async def delete_task(
        task: Annotated[Task, Depends(get_task_by_id)],
        task_service: Annotated[TaskService, Depends(TaskService)]
):
    await task_service.delete_task(task)
    return {"detail": "Задача успешно удалена!", "data": None}