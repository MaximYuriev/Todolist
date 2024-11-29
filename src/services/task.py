from typing import Annotated, Sequence

from fastapi import Depends

from src.models.task import Task
from src.repositories.task import TaskRepository
from src.schemas.task import TaskCreate, TaskUpdate
from src.utils.status import StatusEnum


class TaskService:
    def __init__(self, repository: Annotated[TaskRepository, Depends(TaskRepository)]):
        self.repository = repository

    async def add_task(self, task: TaskCreate):
        task_data = task.model_dump()
        await self.repository.add(task_data)

    async def get_all_tasks(self, status: StatusEnum | None = None) -> Sequence[Task]:
        if status:
            return await self.repository.get_all(status=status.value)
        return await self.repository.get_all()

    async def get_task(self, task_id: int) -> Task | None:
        return await self.repository.get(task_id)

    async def update_task(self, task: Task, task_update: TaskUpdate):
        task_update_data = task_update.model_dump(exclude_none=True)
        await self.repository.update(task, task_update_data)

    async def delete_task(self, task: Task):
        await self.repository.delete(task)
