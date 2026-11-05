from sqlalchemy import String, Boolean
from sqlalchemy.orm import Mapped, mapped_column

from database import Base


# Define the tasks table
class Task(Base):

    # Table name in MySQL
    __tablename__ = "tasks"

    # Unique task ID
    id: Mapped[int] = mapped_column(
        primary_key=True,
        index=True
    )

    # Task text entered by the user
    text: Mapped[str] = mapped_column(
        String(255),
        nullable=False
    )

    # Whether the task is completed
    completed: Mapped[bool] = mapped_column(
        Boolean,
        default=False
    )
