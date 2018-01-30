from objects import words_to_object
import pytest
import unittest

class TestSum(unittest.TestCase):
    def test_1(self):
        self.assertEqual(words_to_object("red 1 yellow 2 black 3 white 4"), "[{name : 'red', id : '1'}, {name : 'yellow', id : '2'}, {name : 'black', id : '3'}, {name : 'white', id : '4'}]")
    def test_2(self):
        self.assertEqual(words_to_object("1 red 2 white 3 violet 4 green"), "[{name : '1', id : 'red'}, {name : '2', id : 'white'}, {name : '3', id : 'violet'}, {name : '4', id : 'green'}]")
    def test_3(self):
        self.assertEqual(words_to_object("1 1 2 2 3 3 4 4"), "[{name : '1', id : '1'}, {name : '2', id : '2'}, {name : '3', id : '3'}, {name : '4', id : '4'}]")
    def test_4(self):
        self.assertEqual(words_to_object("#@&fhds 123F3f 2vn2# 2%y6D @%fd3 @!#4fs W@R^g WE56h%"), "[{name : '#@&fhds', id : '123F3f'}, {name : '2vn2#', id : '2%y6D'}, {name : '@%fd3', id : '@!#4fs'}, {name : 'W@R^g', id : 'WE56h%'}]")
    def test_5(self):
        self.assertEqual(words_to_object(""), "[]")