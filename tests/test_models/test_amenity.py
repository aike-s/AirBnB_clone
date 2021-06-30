#!/usr/bin/python3
""" tests """

import unittest
from models import storage
from models.amenity import Amenity

class TestAmenity(unittest.TestCase):
    """ Unittest for testing Amenity class """

    test_obj = Amenity()
    test_obj.name = "Breakfast"

    def test_init(self):
        """  """

if __name__ == '__main__':
    unittest.main()
