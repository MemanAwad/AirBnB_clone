#!/usr/bin/python3
"""Module for FileStorage Class"""

import json
import os
from models.base_model import BaseModel
from models.user import User
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.state import State
from models.city import City


class FileStorage():
    """
    serializes instances to a JSON file and
    deserializes JSON file to instances
    """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """returns the dictionary object"""
        return FileStorage.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        serialize = {}
        for key in FileStorage.__objects.keys():
            serialize[key] = FileStorage.__objects[key].to_dict()

        with open(FileStorage.__file_path, "w", encoding="utf-8") as file:
            json.dump(serialize, file)

    def reload(self):
        """deserializes the JSON file to __objects"""

        if os.path.isfile(FileStorage.__file_path):
            with open(FileStorage.__file_path, "r") as file:
                try:
                    dicty = json.load(file)
                    for key, value in dicty.items():
                        c_name, ob_id, = key.split('.')
                        cls = eval(c_name)
                        objecty = cls(**value)
                        FileStorage.__objects[key] = objecty

                except Exception:
                    return
