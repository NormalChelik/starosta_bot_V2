from sqlalchemy import update

from db.create_db import create_session
from db.models.users import (Groups,
                             Users)

session = create_session()

def check_groups():
    groups = session.query(Groups.group_name).all()
    return groups

def add_user(user_id: int, group_name: str, full_name: str):
    session.add(Users(
            id=user_id,
            group=group_name,
            full_name=full_name
        ))
    session.commit()

def check_user(user_id: int):
    return session.query(Users.id, Users.full_name, Users.group).filter(Users.id == user_id).all()[0]