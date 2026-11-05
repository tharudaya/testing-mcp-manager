import os

from dotenv import load_dotenv
from sqlalchemy import URL, create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase


# Load database settings from the .env file
load_dotenv()


# MySQL database connection
DATABASE_URL = URL.create(
    "mysql+pymysql",
    username=os.environ["DB_USER"],
    password=os.environ["DB_PASSWORD"],
    host=os.getenv("DB_HOST", "localhost"),
    port=int(os.getenv("DB_PORT", "3306")),
    database=os.environ["DB_NAME"],
)


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
