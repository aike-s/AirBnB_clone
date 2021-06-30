#!/usr/bin/python3
""" tests """

import unittest
from models import storage
from models.city import City

class TestCity(unittest.TestCase):
    """ Unittest for testing City class """

    test_obj = City()
    test_obj.name = "Tunja"

    def test_init(self):
        """  """

if __name__ == '__main__':
    unittest.main()
