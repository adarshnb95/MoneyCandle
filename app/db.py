import os
from typing import Generator

from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base, Session

# Load environment variables from .env
load_dotenv()

DATABASE_URL = os.getenv(
    "DATABASE_URL",
    "postgresql+psycopg2://postgres:supersecret@localhost:5433/postgres",
)

engine = create_engine(
    DATABASE_URL,
    future=True,
    echo=False,  # set True if you want SQL logs
)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine,
    future=True,
)

Base = declarative_base()


def get_db() -> Generator[Session, None, None]:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def init_db() -> None:
    """
    Import models and create tables if they do not exist.
    Call this once on startup.
    """
    from app import models  # noqa: F401  (ensures models are registered with Base)

    Base.metadata.create_all(bind=engine)
