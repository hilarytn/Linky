import json
import os


class FileStorage:
    __file_path = 'file.json'
    __objects = {}

    def all(self):
        if FileStorage.__objects != {} or FileStorage.__objects is not None:
            return FileStorage.__objects
        else:
            pass

    def new(self, obj):
        key = type(obj).__name__
        obj_id = obj.id
        key_obj_id = key + '.' + obj_id
        FileStorage.__objects[key_obj_id] = obj

    def save(self):
        #obj = {key : value for key, value in FileStorage.__objects.items()}
        with open(FileStorage.__file_path, 'w') as f:
            obj = {key : value.to_dict() for key, value in FileStorage.__objects.items()}
            json.dump(obj, f)

    def classes(self):
        """Returns a dictionary of valid classes and their references"""
        from models.base_model import BaseModel
        from models.user import User
        from models.vendor import Vendor
        #from models.city import City
        #from models.amenity import Amenity
        #from models.place import Place
        #from models.review import Review

        classes = {"BaseModel": BaseModel,
                   "User": User,
                   "Vendor": Vendor
                   #"State": State,
                   #"City": City,
                   #"Amenity": Amenity,
                   #"Place": Place,
                   #"Review": Review
                   }
        return classes

    def reload(self):
        if os.path.exists(FileStorage.__file_path):
            with open(FileStorage.__file_path, 'r', encoding="utf-8") as f:
                new_obj = json.load(f)
                reloaded = {k : self.classes()[v["__class__"]](**v) for k, v in new_obj.items()}  #globals()[v["__class__"]](**v)
                FileStorage.__objects = reloaded
        else:
            pass
