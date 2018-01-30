from highlow import high_and_low
import pytest
import unittest

class TestSum(unittest.TestCase):
    def test_1(self):
        self.assertEqual(high_and_low("4 5 29 54 4 0 -214 542 -64 1 -3 6 -6"), "542 -214")
    def test_2(self):
        self.assertEqual(high_and_low("1 -1"), "1 -1")
    def test_3(self):
        self.assertEqual(high_and_low("1 1"), "1 1")
    def test_4(self):
        self.assertEqual(high_and_low("-1 -1"), "-1 -1")
    def test_5(self):
        self.assertEqual(high_and_low("1 -1 0"), "1 -1")
    def test_6(self):
        self.assertEqual(high_and_low("1 1 0"), "1 0")
    def test_7(self):
        self.assertEqual(high_and_low("-1 -1 0"), "0 -1")
    def test_8(self):
        self.assertEqual(high_and_low("42"), "42 42")
