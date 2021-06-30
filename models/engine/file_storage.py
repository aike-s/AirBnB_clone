#!/usr/bin/python3
"""
Here, the class FileStorage that serializes instances to a JSON file
and deserializes JSON file to instances
"""

import json
import os.path

from models.user import User
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.state import State
from models.review import Review


class FileStorage():
    """ Initialization of class attributes """

    __file_path = "objects_info.json"
    __objects = {}

    def all(self):
        """ Returns the dictionary __objects """

        return FileStorage.__objects

    def new(self, obj):
        """ Sets in __objects the obj """

        """ Find the name of the key for the dictionary __objects """
        key = obj.__class__.__name__ + "." + obj.id

        """ Update the dictionary __objects with the new object """
        FileStorage.__objects[key] = obj

    def save(self):
        """ Serializes __objects to the JSON file """

        obj_dict = {}
        for key, obj in self.all().items():
            """ Each object dictionary is saved for later serialization """
            if type(obj) is dict:
                obj_dict[key] = obj
            else:
                obj_dict[key] = obj.to_dict()

        with open(FileStorage.__file_path, mode="w") as open_file:
            """ Here the dictionary obj_dict is serializated and is saved """
            json.dump(obj_dict, open_file)

    def update_file(self, obj, key_name):
        """ Update __file_path file """

        FileStorage.__objects[key_name] = obj
        self.save()

    def reload(self):
        """ Deserializes the JSON file to __objects """
        """ Verify if the file exists """
        from models.base_model import BaseModel
        class_dict = {"User": User, "BaseModel": BaseModel,
                      "Place": Place, "State": State,
                      "City": City, "Amenity": Amenity,
                      "Review": Review}
        try:
            if os.path.isfile(FileStorage.__file_path):
                with open(FileStorage.__file_path, mode="r") as open_file:
                    dict_objs = json.load(open_file)
                    for key, value in dict_objs.items():
                        self.new(BaseModel(**value))
        except:
            pass
