#!/usr/bin/python3
"""This module defines the Storage class"""
from models.base_model import BaseModel, Base
from models.contact import Contact
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session
from sqlalchemy.orm import sessionmaker
import os


classes = {"Contact": Contact}

class Storage:
    """This class manages the MySQL database for Lyrics for Learning"""
    __engine = None
    __session = None

    def __init__(self):
        self.__engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format('linky', 'linky_June2023', 'linky_db', pool_pre_ping=True))

    def classes(self):
        """Returns a dictionary of valid classes and their references"""
        from models.contact import Contact

        classes = {"Contact": Contact}
        return classes

    def all(self, cls=None):
        """return a dictionary
        Return:
            returns a dictionary of objects
        """
        obj_dict = {}
        if cls is None:
            for obj in self.__session.query(Contact).all():
                key = "{}.{}".format(type(obj).__name__, obj.id)
                obj_dict[key] = obj
        else:
            for obj in self.__session.query(cls).all():
                key = "{}.{}".format(cls.__name__, obj.id)
                obj_dict[key] = obj
        return obj_dict

    def new(self, obj):
        """add the object to the current database session
        Args:
            obj: given object
        """
        self.__session.add(obj)

    def save(self):
        """commit all changes of the current database session
        """
        self.__session.commit()

    def delete(self, obj=None):
        """delete the object from the current database session
        Args:
            obj: given object
        """
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """create all tables in the database and the current database session
        """
        print("RELOAD")
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine,
                                       expire_on_commit=False)
        self.__session = scoped_session(session_factory)

    def close(self):
        """close the current session to force reload
        """
        print("CLOSE")
        self.__session.remove()

    def get(self, cls, id):
        """get object based on class and id"""
        objs = self.__session.query(classes[cls]).all()
        for obj in objs:
            if obj.__class__.__name__ == cls and obj.id == id:
                return obj
        return None
