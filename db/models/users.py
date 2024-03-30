from sqlalchemy import Column, VARCHAR, Integer
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Groups(Base):
    __tablename__ = 'groups'
    group_name = Column(VARCHAR(15), primary_key=True, nullable=False)

class Users(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, nullable=False)
    group = Column(VARCHAR(15), nullable=False)
    full_name = Column(VARCHAR(500), nullable=False)
