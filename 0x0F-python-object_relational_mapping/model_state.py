#!/usr/bin/python3
"""declare a model for sqlalchmey to map to database"""
from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship


Base = declarative_base()
class State(Base):
    """create ORM model for state entities"""
    __tablename__ = "states"

    id  = Column('id', Integer, primary_key=True, unique=True, nullable=False)
    name = Column('name', String(128), nullable=False)

    cities = relationship("City", backref="state")
