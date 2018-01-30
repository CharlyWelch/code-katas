from descending import Descending_Order
import pytest
import unittest

class TestSum(unittest.TestCase):
    def test_1(self):
        self.assertEqual(Descending_Order(0), 0)
    def test_2(self):
        self.assertEqual(Descending_Order(15), 51)
    def test_3(self):
        self.assertEqual(Descending_Order(123456789), 987654321)
