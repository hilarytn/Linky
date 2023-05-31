#!/usr/bin/python3
from models.base_model import BaseModel
from models import storage


class Vendor(BaseModel):
    def __init__(self, vendor_fname, vendor_sname, vendor_email, vendor_address):
        super().__init__()
        self.first_name = vendor_fname
        self.surname = vendor_sname
        self.email = vendor_email
        self.address = vendor_address
        storage.new(self)

