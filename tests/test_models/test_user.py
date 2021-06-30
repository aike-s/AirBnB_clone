#!/usr/bin/python3
""" tests """

import unittest
from models import storage
from models.user import User

class TestUser(unittest.TestCase):
    """ Unittest for User class """

    test_obj = User()
    test_obj.email = "jesusita64@yahoo.com"
    test_obj.first_name = "Jesusita"
    test_obj.last_name = "del Rosario"

    def test_init():
        """  """

if __name__ == '__main__':
    unittest.main()
