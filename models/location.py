#!/usr/bin/python3
""" Location """


from datetime import datetime
import models
from sqlalchemy import Column, String, DateTime, ForeignKey, Integer
from models.basemodel import BaseModel, Base
from sqlalchemy.orm import relationship


class Location(BaseModel, Base):
    __tablename__ = 'locations'

    id = Column(String(128), primary_key=True)
    user_name = Column(String(128), ForeignKey('users.username'))
    name = Column(String(128), nullable=True)
    address = Column(String(128), nullable=True)
    latitude = Column(String(28), nullable=False, default='0')
    longitude = Column(String(28), nullable=False, default='0')
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow)

    user = relationship('User', backref='locations')


    def __init__(self, *args, **kwargs):
        """Initializes location"""
        super().__init__(*args, **kwargs)
