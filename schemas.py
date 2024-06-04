from pydantic import BaseModel
from typing import Optional


class ToDoBase(BaseModel):
    task: str

class ToDoCreate(ToDoBase):
    pass


# Schema for updating a todo item
class ToDoUpdate(BaseModel):
    completed: Optional[bool]  # Optional field to update the completion status

class ToDo(ToDoBase):
    id: int
    completed: bool

    class Config:
        orm_mode = True


