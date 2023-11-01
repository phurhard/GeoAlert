#!/usr/bin/python3
""" MySQL database storage"""


# from BE.models import storage
from BE.models.user import User
from BE.models.locationreminder import LocationReminder
from BE.models.todo import Todo
from BE.models.location import Location
from BE.models.basemodel import Base
# from os import getenv
from sqlalchemy.exc import IntegrityError
import logging
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
classes = {
    "User": User,
    "Location": Location,
    "Todo": Todo,
    "LocationReminder": LocationReminder
    }


class DBStorage:
    """ Interacts with the MySQL database"""
    __engine = None
    __session = None

    def __init__(self):
        """ Instantiate the database storage"""
        '''
        USER = getenv('USER')
        PWD = getenv('PWD')
        HOST = getenv('HOST')
        DB = getenv('DB')
        if HOST is not None:
            self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.format(
                USER, PWD, HOST, DB))
        else:
            # uncomment to make use of mySQL
            # self.__engine = create_engine(
            'mysql+mysqldb://admin:GeoAlertAdmin@localhost/GeoAlert'
            )
        '''
        self.__engine = create_engine('sqlite:///:GEOALERT.db', echo=True)

    def load(self):
        """Load the db session"""
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine,
                                       expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session

    def all(self, cls=None):
        """ Query the database for all instances of the cls
        if provided or if not, it'll bring all the data on the database
        """
        new_dict = {}
        for clss in classes:
            if cls is None or cls is classes[clss] or cls is clss:
                objs = self.__session.query(classes[clss]).all()

                for obj in objs:
                    if obj.__class__.__name__ == 'User':
                        key = f"{obj.__class__.__name__ }.{obj.username}"
                    else:
                        key = f"{obj.__class__.__name__}.{obj.id}"
                    new_dict[key] = obj
        return new_dict

    def new(self, obj):
        """Adds new object to the current database session"""
        self.__session.add(obj)
        self.save()

    def save(self):
        """Commit all changes to the database"""
        try:
            self.__session.commit()
        except Exception as e:
            self.__session.rollback()
            print(e)

    def delete(self, obj=None):
        """Deletes an obj instance from the database if obj is not None"""
        if obj is not None:
            self.__session.delete(obj)

    def clear(self, obj):
        '''Deletes all entries in database
        should only be used on tasks'''
        objs = self.__session.query(Todo).all()
        for i in objs:
            self.__session.delete(i)
        self.__session.commit()

    def get(self, cls, unit=None):
        """Returns the object based on it's id.
        will later need to change the id to something
        that can be easy to implement"""
        try:
            if cls not in classes.values():
                return None
            all_cls = self.all(cls)
            if unit is None:
                return all_cls  # [cls]
            if cls == eval('User'):
                for value in all_cls.values():
                    if (value.username == unit):
                        return value
            for value in all_cls.values():
                if (value.id == unit):
                    return value
        except ValueError:
            raise ValueError

    def count(self, cls=None):
        """Count the number of objects in the storage"""
        all_classes = classes.values()
        count = 0

        if not cls:
            for clss in all_classes:
                count += len(self.all(clss).values())
        else:
            count += len(self.all(cls).values())
        return count

    def close(self):
        """Closes the current database session"""
        if self.__session is not None:
            self.__session.close()

    def search(self,  cls, **kwargs):
        """Enables searching in the db"""
        if type(cls) is str:
            cls = classes.get(cls)
        if cls is not None and cls in classes.values():
            return self.__session.query(cls).filter_by(**kwargs).all()
