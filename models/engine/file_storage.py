import json
from models.base_model import BaseModel
from models.user import User
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.state import State
from models.city import City

class FileStorage():
    """serializes instances to a JSON file and deserializes JSON file to instances"""
    
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """returns the dictionary object"""
        return self.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        serialize = {}
        for key, value in FileStorage.__objects.items():
            serialize[key] = value.to_dict()

        with open(FileStorage.__file_path, 'a') as json_file:
            json.dump(serialize, json_file)

    def reload(self):
        """deserializes the JSON file to __objects"""

        with open(FileStorage.__file_path, 'r') as file:
            try:
                dicty = json.load(file)
                for obj in dicty.values():
                    c_name = obj["__class__"]
                    del obj["__class__"]
                    self.new(eval(c_name)(**obj))

            except Exception:
                return

        
