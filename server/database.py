from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase


# MySQL database connection
DATABASE_URL = "mysql+pymysql://root:root@localhost/task_manager_new"


# Create the database engine
engine = create_engine(
    DATABASE_URL,
    echo=True
)


# Create database sessions
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)


# Base class for our database models
class Base(DeclarativeBase):
    pass


# Provide a database session to each API request
def get_db():
    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()
