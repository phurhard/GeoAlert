#!/usr/bin/python3
""" Location """


from sqlalchemy import Column, String, ForeignKey
from BE.models.basemodel import BaseModel, Base
from sqlalchemy.orm import relationship


class Location(BaseModel, Base):
    __tablename__ = 'locations'

    id = Column(String(128), primary_key=True)
    user_name = Column(String(128), ForeignKey('users.username'))
    name = Column(String(128))
    address = Column(String(128))
    latitude = Column(String(28))
    longitude = Column(String(28))

    user = relationship('User', backref='locations')

    def __init__(self, *args, **kwargs):
        """Initializes location"""
        super().__init__(*args, **kwargs)
