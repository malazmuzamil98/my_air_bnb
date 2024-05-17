#!/usr/bin/python3
import json
import os
from models.base_model import BaseModel

"""_summary_"""


classes = {"BaseModel": BaseModel}
class FileStorage:
    """_summary_"""

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """_summary_"""

        return FileStorage.__objects

    def new(self, obj):
        """_summary_

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
            with open(self.__file_path, 'r') as f:
                json_data = json.load(f)
            for key, value in json_data.items():
                cls_name = value['__class__']
                obj = classes[cls_name](**value)
                self.__objects[key] = obj
        except Exception as e:
            print("Error reloading:", e)
