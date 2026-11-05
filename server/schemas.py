from pydantic import BaseModel


# Data received when creating a task
class TaskCreate(BaseModel):
    text: str


# Data received when updating a task
class TaskUpdate(BaseModel):
    text: str
    completed: bool


# Data returned by the API
class TaskResponse(BaseModel):
    id: int
    text: str
    completed: bool

    # Allow Pydantic to read SQLAlchemy objects
    class Config:
        from_attributes = True
