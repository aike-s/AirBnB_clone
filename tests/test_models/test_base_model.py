#!/usr/bin/python3
""" tests """

import unittest
from models.base_model import BaseModel

class TestBaseModel(unittest.TestCase):
    """ Unittest for BaseModel class """

    test_obj = BaseModel()
    test_obj.name = "Anita"
    test_obj.age = 34

    def test_init(self):
        """  """

if __name__ == '__main__':
    unittest.main()
