#!/usr/bin/python3
""" unitest """
import unittest
from models.base_model import BaseModel
from uuid import UUID
import datetime


class TestBaseModel(unittest.TestCase):
    """ test basemodel """
    my_model = BaseModel()

    def testBaseModel(self):
        """ test basemodel """
        self.my_model.name = "My First Model"
        self.my_model.my_number = 89
        self.my_model.save()
        my_model_json = self.my_model.to_dict()

        self.assertEqual(self.my_model.name, my_model_json['name'])
        self.assertEqual(self.my_model.my_number, my_model_json['my_number'])
        self.assertEqual('BaseModel', my_model_json['__class__'])
        self.assertEqual(self.my_model.id, my_model_json['id'])

    def testSave(self):
        """ test if update works or not """
        self.my_model.first_name = "First"
        self.my_model.save()
        self.assertIsInstance(self.my_model.id, str)
        self.assertIsInstance(self.my_model.created_at, datetime.datetime)
        self.assertIsInstance(self.my_model.updated_at, datetime.datetime)
        first_dict = self.my_model.to_dict()
        self.my_model.first_name = "Second"
        self.my_model.save()
        sec_dict = self.my_model.to_dict()
        self.assertEqual(first_dict['created_at'], sec_dict['created_at'])
        self.assertNotEqual(first_dict['updated_at'], sec_dict['updated_at'])

    if __name__ == '__main__':
        nittest.main()
