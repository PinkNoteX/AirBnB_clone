#!/usr/bin/python3
""" amenity unittest """
from models.amenity import Amenity
from tests.test_models.test_base_model import TestBaseModel


class TestAmenity(TestBaseModel):
    """ test amenity """
    def __init__(self, *args, **kwargs):
        """ init """
        super().__init__(*args, **kwargs)
        self.test_class = Amenity
        self.test_name = "Amenity"

    def test_amenity(self):
        """ test amenity """
        amenity = self.test_class()
        self.assertIsInstance(amenity.name, str)
