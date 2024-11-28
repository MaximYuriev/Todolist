from pydantic import BaseModel, ConfigDict

from utils.status import StatusEnum


class TaskCreate(BaseModel):
    model_config = ConfigDict(use_enum_values=True)
    title: str
    description: str
    status: StatusEnum

class TaskUpdate(TaskCreate):
    title: str | None = None
    description: str | None = None
    status: StatusEnum | None = None