from sqlalchemy import update

from db.create_db import create_session
from db.models.users import (Groups,
                             Users)

session = create_session()

def check_groups():
    groups = session.query(Groups).all
    print(groups)
    return groups

def add_group_for_user(group_name: str, user_id: int):
    session.add(Users(
        id=user_id,
        group_name=group_name
    ))
def add_users(user_id: int, full_name: str):
    stmt = update(Users).where(Users.c.id == user_id).values(full_name=full_name)
    session.execute(stmt)
    session.commit()