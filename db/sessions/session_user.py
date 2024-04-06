from sqlalchemy.orm import InstrumentedAttribute
from sqlalchemy.orm.exc import MultipleResultsFound
from db.create_db import create_session
from db.models.users import (Group,
                             User)

session = create_session()


def check_groups() -> list[InstrumentedAttribute]:
    return session.query(Group.group_name).all()


def add_user(user_id: int, group_name: str, full_name: str) -> None:
    session.add(User(
        id=user_id,
        group=group_name,
        full_name=full_name
    ))
    session.commit()


def check_user(user_id: int) -> User | None:
    try:
        result = session.query(User.id, User.full_name, User.group).filter(User.id == user_id).one_or_none()
        return result
    except MultipleResultsFound:
        print("Че за хуйня?")
