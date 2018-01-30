from sumnth import series_sum
import unittest
import pytest

class TestSum(unittest.TestCase):
    def test_1(self):
        self.assertEqual(series_sum(1), "1.00")
        
    def test_2(self):
        self.assertEqual(series_sum(2), "1.25")
        
    def test_3(self):
        self.assertEqual(series_sum(3), "1.39")

