#!/usr/bin/python3
""" BaseModel on which all others will be built on"""


from datetime import datetime, date, time, timezone
from BE import models
from sqlalchemy import Column, String, TIMESTAMP
from sqlalchemy.ext.declarative import declarative_base
from uuid import uuid4

Time = "%Y-%m-%dT%H:%M:%S.%f"

Base = declarative_base()


class BaseModel:
    """BaseModel from which all classes will be found"""
    id = Column(String(255), primary_key=True)
    created_at = Column(TIMESTAMP, default=datetime.utcnow)
    updated_at = Column(TIMESTAMP, default=datetime.utcnow)

    def __init__(self, *args, **kwargs):
        '''Initializing the basemodel'''
        if kwargs:
            for k, v in kwargs.items():
                if k != "__class__":
                    setattr(self, k, v)
            if kwargs.get("created_at", None) and type(self.created_at) is str:
                self.created_at = datetime.strptime(kwargs["created_at"], time)
            else:
                self.created_at = datetime.now(timezone.utc)
            if kwargs.get("updated_at", None) and type(self.updated_at) is str:
                self.updated_at = datetime.strptime(kwargs["updated_at"], time)
            else:
                self.updated_at = datetime.now(timezone.utc)
            if kwargs.get("id", None) is None:
                self.id = str(uuid4())
            models.storage.new(self)
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now(timezone.utc)
            self.updated_at = self.created_at

    def __str__(self):
        """ String representation"""
        if self.__class__.__name__ == 'User':
            return "[{:s}] ({:s}) {}".format(self.__class__.__name__,
                                             self.username, self.__dict__)
        else:
            return "[{:s}] ({:s}) {}".format(self.__class__.__name__,
                                             self.id, self.__dict__)

    def save(self):
        """ updates the attr updated_at with the current datetime"""
        self.updated_at = datetime.now(timezone.utc)
        models.storage.save()

    def to_dict(self):
        """ Returns a dictionary containing all
        keys and values of the instance"""
        new_dict = self.__dict__.copy()
        if "created_at" in new_dict:
            new_dict["created_at"] = new_dict["created_at"].strftime(Time)
        if "updated_at" in new_dict:
            new_dict["updated_at"] = new_dict["updated_at"].strftime(Time)
        new_dict["__class__"] = self.__class__.__name__

        if "_sa_instance_state" in new_dict:
            del new_dict["_sa_instance_state"]

        if "password" in new_dict:
            new_dict["password"] = str(new_dict["password"])

        return new_dict

    def delete(self):
        """ Deletes the current instance from the storage"""
        models.storage.delete(self)

    def update(self, **kwargs):
        """Update the instance with the values supplied"""
        for key, value in kwargs.items():
            if key.endswith('date'):
                value = date.fromisoformat(kwargs[key])
            if key.endswith('time'):
                value = time.fromisoformat(kwargs[key])
            if (key == 'created_at') or (key == 'updated_at'):
                continue
            setattr(self, key, value)
            self.updated_at = datetime.now(timezone.utc)
