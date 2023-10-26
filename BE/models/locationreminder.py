#!/usr/bin/python3
""" Location Reminder class"""


from models.basemodel import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey, Boolean, Integer
from sqlalchemy.orm import relationship


class LocationReminder(BaseModel, Base):
    """Location reminder"""

    __tablename__ = 'locationReminder'
    id = Column(String(128), primary_key=True)
    user_name = Column(String(128), ForeignKey('users.username'))
    location_id = Column(String(128), ForeignKey('locations.id'))
    todo_id = Column(String(128), ForeignKey('todos.id'))
    accuracy = Column(Integer, default=0)
    activated = Column(Boolean, default=False)
    user = relationship('User', backref='locationReminder')
    location = relationship('Location', backref='locationReminder')
    todo = relationship('Todo', backref='locationReminder')
