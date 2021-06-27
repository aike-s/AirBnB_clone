#!/usr/bin/python3
"""
"""

from models.base_model import BaseModel

class Place(BaseModel):
    """  """

    city_id = "" #will be the City.id
    user_id = "" # will be the User.id
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = [] # will be the list of Amenity.id later
