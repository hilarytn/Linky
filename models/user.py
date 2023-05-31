from models.base_model import BaseModel
from models import storage
class User(BaseModel):
    def __init__(self, fname, sname, email,  password):
        super().__init__()
        self.fname = fname 
        self.email = email
        self.sname = sname
        self.password = password
        storage.new(self)
