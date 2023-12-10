#!/usr/bin/python3
""" city unittest """
from models.city import City
from tests.test_models.test_base_model import TestBaseModel


class TestCity(TestBaseModel):
    """ city test """
    def __init__(self, *args, **kwargs):
        """ init """
        super().__init__(*args, **kwargs)
        self.test_class = City
        self.test_name = "City"

    def test_cityName(self):
        """ test city name """
        city = self.test_class()
        self.assertIsInstance(city.name, str)

    def test_stateID(self):
        """ test state id """
        city = self.test_class()
        self.assertIsInstance(city.state_id, str)
