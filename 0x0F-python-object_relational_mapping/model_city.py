#!/usr/bin/python3
"""create a city class linked to cities table in the database server"""
from sqlalchemy import Column, String, ForeignKey
from model_state import Base

class City(Base):
    __tablename__ = "cities"

    id = Column("id", primary_key=True, nullable=False, unique=True)
    name = Column("name", String(128), nullable=False)
    state_id = Column("state_id", ForeignKey("states.id"), nullable=False)

    def __repr__(self):
        """define models representation of object
        data in the database server"""
        return ("%s: (%s) %s" % (self.state.name, self.id, self.name))
