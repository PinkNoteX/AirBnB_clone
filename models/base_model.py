#!/usr/bin/python3
""" the base model """
from uuid import uuid4
from datetime import datetime
from models import storage


class BaseModel:
    """ the class """
    def __init__(self, *args, **kwargs):
        """ init """
        if not kwargs:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            self.save()
            storage.new(self)
        else:
            kwargs['created_at'] = datetime.strptime(kwargs['created_at'],
                                                     '%Y-%m-%dT%H:%M:%S.%f')
            kwargs['updated_at'] = datetime.strptime(kwargs['updated_at'],
                                                     '%Y-%m-%dT%H:%M:%S.%f')
            del kwargs['__class__']
            self.__dict__.update(kwargs)

    def __str__(self):
        """ string """
        return '[{}] ({}) {}'.format(
                    type(self).__name__, self.id, self.__dict__)

    def save(self):
        """ save current to obj """
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """ to dictinary """
        my_dict = dict(self.__dict__)
        my_dict['created_at'] = self.created_at.isoformat()
        my_dict['updated_at'] = self.updated_at.isoformat()
        my_dict['__class__'] = type(self).__name__
        return my_dict
