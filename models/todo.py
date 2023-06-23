#!/usr/bin/python3
""" The Todo Class"""


from datetime import datetime
import models
from models.basemodel import BaseModel, Base
from sqlalchemy import Column, String, Boolean, Integer, ForeignKey, DateTime
from sqlalchemy.orm import relationship


class Todo(BaseModel, Base):
    __tablename__ = 'todos'
    id = Column(String(255), primary_key=True)
    user_name = Column(String(128), ForeignKey('users.username'))
    title = Column(String(255))
    description = Column(String(255))
    due_date = Column(DateTime, default=datetime.utcnow)
    completed = Column(Boolean, default=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow)

    user = relationship('User', backref='todos') 

    def __init__(self, *args, **kwargs):
        """initializes todo"""
        super().__init__(*args, **kwargs) 
