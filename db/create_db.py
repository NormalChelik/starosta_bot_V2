from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session

from db.models.users import Base

engine = create_engine("sqlite:///./database.db")


def create_session() -> scoped_session:
    session = scoped_session(
        sessionmaker(autocommit=False, autoflush=False, bind=engine)
    )
    return session


def create_tables():
    Base.metadata.create_all(engine)