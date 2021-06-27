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

        """ aqui no se crea el diccionario de obj porque si este sufre cambios"""
        """ no podran ser serializados correctamente"""

        """ And the name of the key for the dictionary __objects """
        key = ("{}.{}".format(obj.__class__.__name__, obj.id))

        """ Update the dictionary __objects with the new object """
        FileStorage.__objects[key] = obj

    def save(self):
        """ Serializes __objects to the JSON file """

        obj_dict = {}
        """ In All() there are all the objects from which the dictionary """
        """of each one will be obtained """
        for key, obj in self.all().items():
            """ Each object dictionary is saved for later serialization """
            """ IMPORTANTE """
            """ Se hace en este punto porque la informacion esta como debe ser guardada finalmente """
            if type(obj) is dict:
                obj_dict[key] = obj
            else:
                obj_dict[key] = obj.to_dict()

        with open(FileStorage.__file_path, mode="w", encoding='UTF-8') as open_file:
            """ Here the dictionary obj_dict is serializated and is saved """
            """ in the __file_path file """
            json.dump(obj_dict, open_file)

    def reload(self):
        """ Deserializes the JSON file to __objects """
        from models.base_model import BaseModel

        """ Verify if the file exists """
        if os.path.isfile(FileStorage.__file_path):
            with open(FileStorage.__file_path, mode="r", encoding='UTF-8') as open_file:
                dict_objs = json.load(open_file)
                for key, value in dict_objs.items():
                    self.new(BaseModel(**value))
