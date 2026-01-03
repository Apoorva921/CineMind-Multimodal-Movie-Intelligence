from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base

DATABASE_URL = "postgresql://postgres:1234567890@localhost:5432/cinemind"

engine = create_engine(
    DATABASE_URL,
    echo=True  # shows SQL queries in terminal (good for learning)
)

Base = declarative_base()
