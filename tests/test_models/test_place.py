#!/usr/bin/python3
""" tests """

import unittest
from models import storage
from models.place import Place

class TestPlace(unittest.TestCase):
    """ Unittest for Place class """

    test_obj = Place()
    test_obj.name = "Cabañitas"
    test_obj.description = "Super nice, with ocean view"
    test_obj.number_rooms = 2
    test_obj.number_bathrooms = 1
    test_obj.max_guest = 5
    test_obj.price_by_night = 36
    test_obj.latitude = 4.9
    test_obj.longitude = 5.8

    def test_init(self):
        """  """

if __name__ == '__main__':
    unittest.main()
