#!/usr/bin/python3
import uuid
from datetime import datetime
import models
"""_summary_ """


class BaseModel:
    """_summary_  """

    def __init__(self, *args, **kwargs):
        """ _summary_ """

        if kwargs:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    setattr(self, key, datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%f'))
                elif key != "__class__":
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """_summary_"""
    
        return ("[{}] ({}) {}").format(
            self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """_summary_"""

        self.updated_at = datetime.now()
        models.storage.new(self)
        models.storage.save()

    def to_dict(self):
        """_summary_"""

        dict_copy = self.__dict__.copy()
        dict_copy["__class__"] = self.__class__.__name__
        dict_copy["updated_at"] = self.updated_at.isoformat()
        dict_copy["created_at"] = self.created_at.isoformat()
        return dict_copy

