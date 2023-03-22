#!/usr/bin/python3
"""Test the module"""
from tests.test_models.test_base_model import test_basemodel
from models.city import City


class test_City(test_basemodel):
    """Test the class"""

    def __init__(self, *args, **kwargs):
        """Test the defined function """
        super().__init__(*args, **kwargs)
        self.name = "City"
        self.value = City

    def test_state_id(self):
        """Test the defined function """
        new = self.value()
        self.assertEqual(type(new.state_id), str)

    def test_name(self):
        """Test the defined function """
        new = self.value()
        self.assertEqual(type(new.name), str)
