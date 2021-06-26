#!/usr/bin/python3
"""
Here, te module for FileStorage that serializes instances to a JSON file
and deserializes JSON file to instances
"""

import json
import os.path

class FileStorage():

    """  """
    __file_path = "file.json"
    __objects = {}
    def __init__(self):

        """ """

    def all(self):
        return FileStorage.__objects

    def new(self, obj):

        """  """
        """ Obtain the dictionary of the object no es necesario darle el nombre de la clase porque obj ya tiene sus metodos"""
        obj_dict = obj.to_dict()

        """ And the name of the key for the dictionary __objects """
        key = ("{}.{}".format(self.__class__.__name__,obj_dict.get('id')))

        """ Update the dictionary __objects with the new object """
        FileStorage.__objects.update({key : obj_dict})

    def save(self):

        """  """
        """ Here the dictionary __objects is serializated """
        json_txt = json.dumps(FileStorage.__objects)

        with open(FileStorage.__file_path, mode="a", encoding='UTF-8') as open_file:
            """ And now the serialization is saved in the __file_path file """
            open_file.write(json_txt)
            
    def reload(self):
        from models.base_model import BaseModel

        """  """

        """ Verify if the file exists, taht is, if the file has information stored in it """
        if os.path.isfile(FileStorage.__file_path):
            with open(FileStorage.__file_path, mode="r", encoding='UTF-8') as open_file:
                json_text = open_file.read
            """ Deserialization of the json_text to be stored in __objects as objects """
            FileStorage.__objects = json.loads(json_text)
        