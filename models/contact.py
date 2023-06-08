#!/usr/bin/python3
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
    image_url = Column(String(255))

