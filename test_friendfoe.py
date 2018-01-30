from friendfoe import friend
import pytest
import unittest

class TestSum(unittest.TestCase):
    def test_1(self):
        self.assertEqual(friend(["Ryan", "Kieran", "Mark",]), ["Ryan", "Mark"])