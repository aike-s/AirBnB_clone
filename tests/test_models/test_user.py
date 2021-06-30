#!/usr/bin/python3
""" tests """

import unittest
from models import storage
from models.user import User

class TestUser(unittest.TestCase):
    """ Unittest for User class """

    obj = User()
    

    def test_init():
        """  """

if __name__ == '__main__':
    unittest.main()
