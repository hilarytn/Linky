#!/usr/bin/python3
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv
from models.base_model import Base
from models.contact import Contact
from models import storage
import sys

if __name__ == "__main__":
    try:
        contact = Contact()
        contact.first_name = sys.argv[1]
        contact.location = sys.argv[2]
        contact.specialization = sys.argv[3]
        contact.employer = sys.argv[4]
        storage.new(contact)
        storage.save() 
    except IndexError:
        print("Please supply arguments")


    storage.delete(contact)
