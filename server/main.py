from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session

import models
import schemas

from database import engine, get_db


# Create database tables if they don't already exist
models.Base.metadata.create_all(bind=engine)


# Create FastAPI application
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins="http://localhost:5173/",
    allow_headers=["*"],
    allow_methods=["*"]
)

# Simple health check


@app.get("/")
def root():
    return {
        "message": "Task Manager API is running"
    }


# ---------------------------------------------------------
# GET ALL TASKS
# ---------------------------------------------------------

@app.get(
    "/tasks",
    response_model=list[schemas.TaskResponse]
)
def get_tasks(
    db: Session = Depends(get_db)
):
    # Get all tasks from the database
    tasks = db.query(models.Task).all()

    # Return the tasks as JSON
    return tasks


# ---------------------------------------------------------
# CREATE TASK
# ---------------------------------------------------------

@app.post(
    "/tasks",
    response_model=schemas.TaskResponse,
    status_code=201
)
def create_task(
    task: schemas.TaskCreate,
    db: Session = Depends(get_db)
):
    # Create a new Task database object
    new_task = models.Task(
        text=task.text
    )

    # Add the task to the database session
    db.add(new_task)

    # Save the task to MySQL
    db.commit()

    # Get the generated ID and other database values
    db.refresh(new_task)

    # Return the newly created task
    return new_task


# ---------------------------------------------------------
# UPDATE TASK
# ---------------------------------------------------------

@app.put(
    "/tasks/{task_id}",
    response_model=schemas.TaskResponse
)
def update_task(
    task_id: int,
    task: schemas.TaskUpdate,
    db: Session = Depends(get_db)
):
    # Find the task using its ID
    existing_task = db.query(models.Task).filter(
        models.Task.id == task_id
    ).first()

    # Return 404 if the task doesn't exist
    if not existing_task:
        raise HTTPException(
            status_code=404,
            detail="Task not found"
        )

    # Update the task text
    existing_task.text = task.text

    # Update completed status
    existing_task.completed = task.completed

    # Save changes to MySQL
    db.commit()

    # Refresh the object with the latest database values
    db.refresh(existing_task)

    # Return the updated task
    return existing_task


# ---------------------------------------------------------
# DELETE TASK
# ---------------------------------------------------------

@app.delete("/tasks/{task_id}")
def delete_task(
    task_id: int,
    db: Session = Depends(get_db)
):
    # Find the task using its ID
    task = db.query(models.Task).filter(
        models.Task.id == task_id
    ).first()

    # Return 404 if the task doesn't exist
    if not task:
        raise HTTPException(
            status_code=404,
            detail="Task not found"
        )

    # Delete the task from the database
    db.delete(task)

    # Save the deletion
    db.commit()

    # Return a simple success response
    return {
        "message": "Task deleted successfully"
    }
