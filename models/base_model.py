#!/usr/bin/python3
"""
module of Base Model class
"""

from datetime import datetime
from uuid import uuid4
import models


class BaseModel:
    """Define Base Model"""

    def __init__(self, *args, **kwargs):
        """Constructor"""

        date_format = "%Y-%m-%dT%H:%M:%S.%f"
        self.id = str(uuid4())
        self.created_at = datetime.utcnow()
        self.updated_at = datetime.utcnow()

        if kwargs:
            for key, value in kwargs.items():
                if key == '__class__':
                    continue
                elif key == 'created_at' or key == 'updated_at':
                    setattr(self, key,
                            datetime.strptime(value, date_format))
                else:
                    setattr(self, key, value)

        models.storage.new(self)

    def __str__(self):
        """ print: [<class name>] (<self.id>) <self.__dict__>"""

        return "[{}] ({}) {}".format(self.__class__.__name__,
                                     self.id, (self.__dict__))

    def save(self):
        """updates the public instance attribute
        updated_at with the current datetime
        """

        self.updated_at = (datetime.utcnow())
        models.storage.save()

    def to_dict(self):
        """returns a dictionary containing all keys/values
        of __dict__ of the instance
        """

        dict_user = self.__dict__.copy()
        dict_user["created_at"] = self.created_at.isoformat()
        dict_user["updated_at"] = self.updated_at.isoformat()
        dict_user['__class__'] = self.__class__.__name__
        return dict_user
