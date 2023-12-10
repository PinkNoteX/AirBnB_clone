#!/usr/bin/python3
""" user """
from models.base_model import BaseModel


class User(BaseModel):
    """ user class """
    email = ''
    password = ''
    first_name = ''
    last_name = ''

    def __init__(self, *args, **kwargs):
        """ init """
        super().__init__(*args, **kwargs)
