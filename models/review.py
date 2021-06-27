#!/usr/bin/python3
"""
In this module the class Review which inherits from the class BaseModel
"""

from models.base_model import BaseModel

class Review(BaseModel):
    """ Initialization of the class attributes """

    place_id = "" # it will be the Place.id
    user_id = "" # will be the User.id
    text = ""
