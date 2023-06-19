#!/usr/bin/python3
""" The user class"""


from datetime import datetime
import models
from models.basemodel import BaseModel, Base
import sqlalchemy
from sqlalchemy import Column, String, DateTime
from sqlalchemy.orm import relationship


class User(BaseModel, Base):
    """Representation of the user model"""
    __tablename__ = 'users'
    username = Column(String(128), primary_key=True, nullable=False, default='anonymous')
    firstname = Column(String(128), nullable=False, default='Anonymous')
    lastname = Column(String(128), nullable=True)
    email = Column(String(128), nullable=False, default='anoymous@mail')
    password = Column(String(128), nullable=False, default='password')
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow)

    def __init__(self, *args, **kwargs):
        '''initializes user'''
        super().__init__(*args, **kwargs)

    def __setattr__(self, name, value):
        """Encrypts the password with md5 encryption"""
        if name == "password":
            value = md5(value.encode()).hexdigest()
        super().__setattr__(name, value)
