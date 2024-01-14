#!user/bin/python3
from datetime import datetime
from uuid import uuid4
import models


class BaseModel():

    def __init__(self, *args, **kwargs):
        date_format = "%Y-%m-%dT%H:%M:%S.%f"
        self.id = str(uuid4())
        self.created_at = datetime.utcnow()
        self.updated_at = datetime.utcnow()

        if kwargs:
            for key, value in kwargs.items():
                if key != '__class__':
                    if key == 'created_at' or key == 'updated_at':
                        setattr(self, key,
                                datetime.strptime(value, date_format))
                    else:
                        setattr(self, key, value)
        models.storage.new(self)

    def __str__(self):
        return "[{}] ({}) {}".format(self.__class__.__name__,
                self.id, (self.__dict__))

    def save(self):
        self.updated_at = (datetime.utcnow())
        models.storage.save()

    def to_dict(self):
        dict_user = self.__dict__.copy()
        dict_user["created_at"] = self.created_at.isoformat()
        dict_user["updated_at"] = self.updated_at.isoformat()
        dict_user['__class__'] = self.__class__.__name__
        return dict_user

