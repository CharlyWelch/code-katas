from the_wall import who_is_paying
import pytest
import unittest 

""" I need to rewrite these tests using pytest, I guess? """
Test.describe("Basic tests")
Test.assert_equals(who_is_paying("Mexico"),["Mexico", "Me"])
Test.assert_equals(who_is_paying("Melania"),["Melania", "Me"])
Test.assert_equals(who_is_paying("Melissa"),["Melissa", "Me"])
Test.assert_equals(who_is_paying("Me"),["Me"])
Test.assert_equals(who_is_paying(""), [""])
Test.assert_equals(who_is_paying("I"), ["I"])