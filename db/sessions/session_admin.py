from db.create_db import create_session
from db.models.users import (Group)

session = create_session()


def add_group(group_name: str) -> None:
    session.add(Group(
        group_name=group_name
    ))
    session.commit()


def add_groups(groups: list[str]) -> None:
    for group in groups:
        session.add(Group(group_name=group))
    session.commit()
