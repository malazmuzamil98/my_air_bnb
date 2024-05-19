#!/usr/bin/python3
"""class BaseModel"""
import uuid
from datetime import datetime
import models


class BaseModel:
    """BaseMode  is the base class of all other classes in our application"""

    def __init__(self, *args, **kwargs):
        """initialze  attributes that aren't set by the create() method"""

        date_format = "%Y-%m-%dT%H:%M:%S.%f"
        if kwargs:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    setattr(self, key, datetime.strptime(value, date_format))
                elif key != "__class__":
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            current_time = datetime.now()
            self.created_at = current_time
            self.updated_at = current_time
            models.storage.new(self)

    def __str__(self):
        """return string representation of the model object"""

        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """Update and save the instance to the file storage."""

        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """generate  a dictionary representation of the model object"""

        dict_copy = self.__dict__.copy()
        dict_copy["__class__"] = self.__class__.__name__
        dict_copy["updated_at"] = self.updated_at.isoformat()
        dict_copy["created_at"] = self.created_at.isoformat()
        return dict_copy
