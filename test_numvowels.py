from numvowels import getCount
import pytest
import unittest

class TestSum(unittest.TestCase):
    def test_1(self):
        self.assertEqual(getCount("abracadabra"), 5)