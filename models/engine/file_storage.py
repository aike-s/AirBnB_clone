#!/usr/bin/python3
"""
Here, the class FileStorage that serializes instances to a JSON file
and deserializes JSON file to instances
"""

import json
import os.path

class FileStorage():
    """ Initialization of class attributes """

    __file_path = "objects_info.json"
    __objects = {}

    def all(self):
        """ Returns the dictionary __objects """

        return FileStorage.__objects

    def new(self, obj):
        """ Sets in __objects the obj """

        """ Obtain the dictionary of the object // no es necesario """
        """ darle el nombre de la clase porque obj ya tiene sus metodos"""
        obj_dict = obj.to_dict()

        """ And the name of the key for the dictionary __objects """
        key = ("{}.{}".format(self.__class__.__name__, obj_dict.get('id')))

        """ Update the dictionary __objects with the new object """
        FileStorage.__objects.update({key : obj_dict})

    def save(self):
        """ Serializes __objects to the JSON file """

        with open(FileStorage.__file_path, mode="a", encoding='UTF-8') as open_file:
            """ Here the dictionary __objects is serializated and is saved """
            """ in the __file_path file """
            json.dump(FileStorage.__objects, open_file)

    def reload(self):
        """ Deserializes the JSON file to __objects """
        from models.base_model import BaseModel

        """ Verify if the file exists """
        if os.path.isfile(FileStorage.__file_path):
            with open(FileStorage.__file_path, mode="r", encoding='UTF-8') as open_file:
                """ Deserialization of file content """
                """ to be stored in __objects as dictionary """
                FileStorage.__objects = json.load(open_file)

            BaseModel(FileStorage.__objects)
