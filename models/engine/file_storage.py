#!/usr/bin/python3
""" re hyw56 ehe5yt5y uh5e7 u6r7 """
import json
import os


class FileStorage:
    """ storage rsth yrst hyrts """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """all func.wr hywsrt hy yh"""
        return FileStorage.__objects

    def new(self, obj):
        """new func. srth rs hyrs hy"""
        key = f"{obj.__class__.__name__}.{obj.id}"
        FileStorage.__objects[key] = obj

    def save(self):
        """save func.srth sr wsy hwsrt yh"""
        odict = FileStorage.__objects
        objdict = {obj: odict[obj].to_dict() for obj in odict.keys()}
        with open(FileStorage.__file_path, "w") as f:
            json.dump(objdict, f)

    def reload(self):
        """ Deserializes __objects from
        t srth srth ysrt he JSON file
        """
        from models.base_model import BaseModel
        from models.user import User
        from models.place import Place
        from models.city import City
        from models.amenity import Amenity
        from models.state import State
        from models.review import Review
        dct = {
                'BaseModel': BaseModel,
                'User': User,
                'Amenity': Amenity,
                'Place': Place,
                'City': City,
                'State': State,
                'Review': Review
                }
        if os.path.exists(FileStorage.__file_path) is True:
            with open(FileStorage.__file_path, 'r') as f:
                for key, value in json.load(f).items():
                    self.new(dct[value['__class__']](**value))
