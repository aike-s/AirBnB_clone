#!/usr/bin/python3
""" tests """

import unittest
from models import storage
from models.state import State

class TestState(unittest.TestCase):
    """ Unittest for State class """
    test_obj = State()
    test_obj = "Antioquia"

    def test_init(self):
        """  """

if __name__ == '__main__':
    unittest.main()
