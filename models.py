from sqlalchemy import Column, Integer, String,Boolean
from database import Base


# Define To Do class inheriting from Base
class ToDo(Base):
    __tablename__ = "todos"

    id = Column(Integer, primary_key=True, index=True)
    task = Column(String, index=True)
    completed = Column(Boolean, default=False)  # New field for completion status
