#!/usr/bin/python3
""" tests """

import unittest
from models import storage
from models.review import Review

class TestReview(unittest.TestCase):
    """ Unittest for Review class """

    test_obj = Review()
    test_obj.text = "Nice place with nice people"

    def test_init(self):
        """  """

if __name__ == '__main__':
    unittest.main()
