from beginner_sum import get_sum
import pytest
import unittest

class TestSum(unittest.TestCase):
    def test_1(self):
        self.assertEqual(get_sum(0,1),1)
    def test_2(self):
        self.assertEqual(get_sum(0,-1),-1)
    def test_3(self):
        self.assertEqual(get_sum(0,2),3)
        