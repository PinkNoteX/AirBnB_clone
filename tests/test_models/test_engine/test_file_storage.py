#!/usr/bin/python3
""" unitest test """
import unittest
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models import storage
import os

class TesFileStorage(unittest.TestCase):
    """ test storage """
    def __init__(self, *args, **kwargs):
        """ init """
        super().__init__(*args, **kwargs)
        self.test_class = FileStorage

    def test_path(self):
        """ test path """
        test = self.test_class()
        self.assertIsInstance(test._FileStorage__file_path, str)

    def test_save(self):
        """ test file save """
        storage.save()
        self.assertTrue(os.path.exists('file.json'))

    def test_obj(self):
        """ test objs """
        test = self.test_class()
        self.assertIsInstance(test._FileStorage__objects, dict)

    def tearDown(self):
        """ destroy json """
        try:
            os.remove('file.json')
        except:
            pass

    def test_file_empty(self):
        """ empty file test """
        base = BaseModel()
        my_dict = base.to_dict()
        base.save()
        base2 = BaseModel(**my_dict)
        self.assertFalse(os.stat('file.json').st_size == 0)
