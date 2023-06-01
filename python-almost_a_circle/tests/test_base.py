#!/usr/bin/python3
"""Unittest for Base Class"""


import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    
    def test_id(self):
        self.obj = Base()
        self.assertEqual(self.obj.id, 1)
        
    def test_id2(self): #Stopping here but need more tests for base
