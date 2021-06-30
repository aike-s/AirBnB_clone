#!/usr/bin/python3
"""
In this module the class Review which inherits from the class BaseModel
"""

from models.base_model import BaseModel


class Review(BaseModel):
    """ Initialization of the class attributes """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
    """it will be the Place.id"""
    place_id = ""
    """will be the User.id"""
    user_id = ""
    text = ""
