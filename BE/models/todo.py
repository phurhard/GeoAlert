#!/usr/bin/python3
""" The Todo Class"""


from datetime import datetime
# from BE import models
from BE.models.basemodel import BaseModel, Base
from sqlalchemy import Column, String, Boolean, Integer, ForeignKey, DateTime
from sqlalchemy.orm import relationship


class Todo(BaseModel, Base):
    __tablename__ = 'todos'
    id = Column(String(255), primary_key=True)
    user_name = Column(String(128), ForeignKey('users.username'))
    # location_id = Column(String(128), ForeignKey('locations.id'))
    title = Column(String(255), nullable=False)
    description = Column(String(255))
    due_date = Column(DateTime)
    completed = Column(Boolean, default=False)
    created_at = Column(DateTime, default=datetime.now)
    updated_at = Column(DateTime, default=datetime.now)

    user = relationship('User', backref='todos')
    # location = relationship('Location', backref='todos')
    
    def __init__(self, *args, **kwargs):
        """initializes todo"""
        super().__init__(*args, **kwargs) 
