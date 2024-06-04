from fastapi import FastAPI, status, HTTPException, Depends
from database import Base, engine, SessionLocal
from sqlalchemy.orm import Session
import models
import schemas
from typing import List
from fastapi.middleware.cors import CORSMiddleware  # Import CORSMiddleware

# Create the database
Base.metadata.create_all(engine)

# Initialize app
app = FastAPI()

# List of allowed origins
# Replace '*' with your frontend's domain if possible
origins = [
    "http://localhost",
    "http://localhost:3000",  # Assuming your React app is running on port 3000
    # Add more origins as needed
]

# Configure CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE"],
    allow_headers=["*"],
)


# Helper function to get database session
def get_session():
    session = SessionLocal()
    try:
        yield session
    finally:
        session.close()


@app.get("/")
async def root():
    return "todo"


@app.post("/todo", response_model=schemas.ToDo, status_code=status.HTTP_201_CREATED)
def create_todo(todo: schemas.ToDoCreate, session: Session = Depends(get_session)):

    # create an instance of the ToDo database model
    tododb = models.ToDo(task=todo.task)

    # add it to the session and commit it
    session.add(tododb)
    session.commit()
    session.refresh(tododb)

    # return the todo object
    return tododb


@app.get("/todo/{id}", response_model=schemas.ToDo)
async def read_todo(id: int):

    # create a new database session
    session = Session(bind=engine, expire_on_commit=False)

    # get the todo item with the given id
    todo = session.query(models.ToDo).get(id)

    # close the session
    session.close()

    # check if todo item with given id exists. If not, raise exception and return 404 not found response
    if not todo:
        raise HTTPException(status_code=404, detail=f"todo item with id {id} not found")

    return todo


@app.delete("/todo/{id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_todo(id: int):

    # create a new database session
    session = Session(bind=engine, expire_on_commit=False)

    # get the todo item with the given id
    todo = session.query(models.ToDo).get(id)

    # if todo item with given id exists, delete it from the database. Otherwise raise 404 error
    if todo:
        session.delete(todo)
        session.commit()
        session.close()
    else:
        raise HTTPException(status_code=404, detail=f"todo item with id {id} not found")

    return None


@app.get("/todo", response_model=List[schemas.ToDo])
async def read_todo_list():
    # create a new database session
    session = Session(bind=engine, expire_on_commit=False)

    # get all todo items
    todo_list = session.query(models.ToDo).all()

    # close the session
    session.close()

    return todo_list


@app.get("/completed")  # Change the HTTP method to GET
def get_completed_todos(db: Session = Depends(get_session)):
    # Get all completed todos
    completed_todos = db.query(models.ToDo).filter(models.ToDo.completed == True).all()
    return completed_todos


@app.put("/todo/{id}")
async def update_todo(
    id: int, todo_update: schemas.ToDoUpdate, session: Session = Depends(get_session)
):
    # Get the todo item with the given id
    todo = session.query(models.ToDo).filter(models.ToDo.id == id).first()

    if not todo:
        raise HTTPException(status_code=404, detail="Todo not found")

    # Update the completion status if it's provided in the request
    if todo_update.completed is not None:
        todo.completed = todo_update.completed

    session.commit()
    return todo


@app.post("/completed")
def move_completed_todos(db: Session = Depends(get_session)):
    # Get all completed todos
    completed_todos = db.query(models.ToDo).filter(models.ToDo.completed == True).all()
    # Move completed todos to the "completed" table
    for todo in completed_todos:
        db.execute(
            models.Completed.__table__.insert().values(id=todo.id, task=todo.task)
        )

    # Delete completed todos from the "todos" table
    db.query(models.ToDo).filter(models.ToDo.completed == True).delete()

    db.commit()

    return {"message": "Completed todos moved successfully"}
