#!/usr/bin/python3
""" The user class"""


from datetime import datetime
import models
from models.basemodel import BaseModel, Base
from sqlalchemy import Column, String, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.schema import UniqueConstraint
# from hashlib import md5
import bcrypt


class User(BaseModel, Base):
    """Representation of the user model"""
    __tablename__ = 'users'
    username = Column(String(128), primary_key=True, nullable=False)
    firstname = Column(String(128), nullable=False)
    lastname = Column(String(128), nullable=True)
    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow)

    __table_args__ = (
            UniqueConstraint('username', name='uq_username'),
            )

    def __init__(self, *args, **kwargs):
        '''initializes user'''
        super().__init__(*args, **kwargs)

    def __setattr__(self, name, value):
        """Encrypts the password with md5 encryption"""
        if name == "password":
            salt = bcrypt.gensalt()
            pwd = value.encode('utf-8')
            # md5(value.encode()).hexdigest()
            value = bcrypt.hashpw(pwd, salt)

        super().__setattr__(name, value)
