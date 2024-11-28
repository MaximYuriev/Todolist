from sqlalchemy.orm import Mapped, mapped_column

from db import Base


class Task(Base):
    __tablename__ = "task"
    task_id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str]
    description: Mapped[str]
    status: Mapped[str]
