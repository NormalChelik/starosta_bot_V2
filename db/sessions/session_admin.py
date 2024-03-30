from db.create_db import create_session
from db.models.users import (Groups)

session = create_session()

def add_groups(group_name: str):
    session.add(Groups(
        group_name=group_name
    ))
    session.commit()