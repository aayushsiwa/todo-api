from pydantic import BaseModel


# Create ToDo Schema (Pydantic Model)
class ToDoCreate(BaseModel):
    id:int
    task: str


# Create ToDo Schema (Pydantic Model)
class ToDo(BaseModel):
    id:int
    task: str

    class Config:
        orm_mode = True
