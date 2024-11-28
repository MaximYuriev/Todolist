from typing import Annotated

from fastapi import Depends, HTTPException
from starlette import status

from services.task import TaskService


async def get_task_by_id(
        task_id: int,
        task_service: Annotated[TaskService, Depends(TaskService)]
):
    task = await task_service.get_task(task_id)
    if task is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Задача не найдена!")
    return task