from the_wall import who_is_paying
import pytest
import unittest 

class TestSum(unittest.TestCase):
    def test_1(self):
        self.assertEqual(who_is_paying("Mexico"),["Mexico", "Me"])
    def test_2(self):
        self.assertEqual(who_is_paying("Melania"),["Melania", "Me"])
    def test_3(self):
        self.assertEqual(who_is_paying("Melissa"),["Melissa", "Me"])
    def test_4(self):
        self.assertEqual(who_is_paying("Me"),["Me"])
    def test_5(self):
        self.assertEqual(who_is_paying(""), [""])
    def test_6(self):
        self.assertEqual(who_is_paying("I"), ["I"])