from typing import Annotated, Sequence

from fastapi import Depends
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from db import get_session
from src.models.task import Task


class TaskRepository:
    def __init__(self, session: Annotated[AsyncSession, Depends(get_session)]):
        self.session = session

    async def add(self, task_data: dict):
        task = Task(**task_data)
        self.session.add(task)
        await self.session.commit()

    async def get_all(self, **kwargs) -> Sequence[Task]:
        query = select(Task).filter_by(**kwargs)
        tasks = await self.session.scalars(query)
        return tasks.all()

    async def get(self, task_id: int) -> Task | None:
        return await self.session.get(Task, task_id)

    async def update(self, task: Task, update_data: dict):
        for key, value in update_data.items():
            setattr(task, key, value)
        await self.session.commit()

    async def delete(self, task: Task):
        await self.session.delete(task)
        await self.session.commit()
