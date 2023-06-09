#!/usr/bin/python3
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv
from models.base_model import Base
from models.contact import Contact
from models import storage
import sys

if __name__ == "__main__":
    objects = storage.all()
    for k in objects.values():
        print(k)
