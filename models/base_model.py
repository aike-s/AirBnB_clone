#!/usr/bin/python3
"""
In this module, the base class BaseModel
"""

""" Para asignar el valor del atributo id """
import uuid
""" Para crear la fecha """
from datetime import datetime

from models import storage

class BaseModel():
    """ Creating the Base class """

    def __init__(self, *args, **kwargs):
        """ Initialization of the instance """

        current_time = datetime.now()
        if kwargs != {}:
            for key, value in kwargs.items():
                if key is '__class__':
                    continue
                else:
                    if key is 'created_at' or key is 'updated_at':
                        value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = current_time
            self.updated_at = current_time
            storage.new(self)

    def __str__(self):
        """ Prints a representation of an instance """

        return ("[{:s}] ({:s}) {}".format(self.__class__.__name__, self.id, self.__dict__))

    def save(self):
        """ Updates the public instance attribute """

        current_time_updated = datetime.now()
        self.updated_at = current_time_updated
        storage.save()

    def to_dict(self):
        """ Returns a dictionary of the instance """

        """ creamos una copia del diccionario para que este no se sobreescriba """
        objects_dict = self.__dict__.copy()
        objects_dict.update({'__class__' : self.__class__.__name__,
                            'created_at' : self.created_at.isoformat(),
                            'updated_at' : self.updated_at.isoformat()})
        return objects_dict
