#!/usr/bin/python3
"""
In this module the class City which inherits from the class BaseModel
"""

from models.base_model import BaseModel

class City(BaseModel):
    """ Initialization of the class attributes """

    state_id = "" # will be the State.id
    name = ""
