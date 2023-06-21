#!/usr/bin/python3
from uuid import uuid4
import sqlalchemy
from sqlalchemy import Column, String
from models.base_model import BaseModel, Base


class Contact(BaseModel, Base):
    __tablename__ = 'contact'

    first_name = Column(String(120), nullable=False)
    location = Column(String(50), nullable=False)
    specialization = Column(String(255), default="In Progress", nullable=False)
    employer = Column(String(255), default="Unemployed")
    socials_url = Column(String(255)) #Consider using JSON here 
    #image_url = Column(String(255))

    def __init__(self, first_name=None, location=None, specialization=None, employer=None, image_url=None):
        #self.id = str(uuid4())
        super().__init__()
        self.first_name = first_name
        self.location = location
        self.specialization = specialization
        self.employer = employer
        self.image_url = image_url


