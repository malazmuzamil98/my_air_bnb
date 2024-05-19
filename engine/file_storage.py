#!/usr/bin/python3
"""Class for a generic list of objects. """
import json
import os
from models.base_model import BaseModel


classes = {"BaseModel": BaseModel}


class FileStorage:
    """
    Class for serializing instances to a JSON file
    and deserializingJSON file to instances.
    """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """return  all objects"""

        return FileStorage.__objects

    def new(self, obj):
        """Adds an object to the storage

        Args:
            obj (_type_): _description_
         Adds a new object to the __objects dictionary"""

        key = obj.__class__.__name__ + "." + obj.id
        FileStorage.__objects[key] = obj

    def save(self):
        """_summary_
        """

        values = {}
        for key, value in self.__objects.items():

            values[key] = value.to_dict()
        with open(self.__file_path, "w", encoding=("utf-8")) as f:
            json.dump(values, f, indent=2)

    def reload(self):
        """Reloads objects from JSON file."""
        try:
            with open(self.__file_path, "r+", encoding="utf-8") as f:
                if os.stat(self.__file_path).st_size == 0:
                    return
                data = json.load(f)
                for key, value in data.items():
                    self.__objects[key] = eval(value["__class__"])(**value)

        except FileNotFoundError:
            pass
