from xo import xo
import pytest
import unittest

class TestSum(unittest.TestCase):
    def test_1(self):
        self.expect(xo('xo'))
    def test_2(self):
        self.expect(xo('xo0'))
    def test_3(self):
        self.expect(not xo('xxxoo'))
