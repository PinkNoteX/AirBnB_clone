#!/usr/bin/python3
from tests.test_models.test_base_model import TestBaseModel
from models.user import User


class TestUser(TestBaseModel):
    """ user tests """
    def __init__(self, *args, **kwargs):
        """ init """
        super().__init__(*args, **kwargs)
        self.test_class = User
        self.test_name = "User"

    def test_email(self):
        """ test email """
        user = self.test_class()
        self.assertIsInstance(user.email, str)

    def test_firstName(self):
        """ test first name """
        user = self.test_class()
        self.assertIsInstance(user.first_name, str)

    def test_lastName(self):
        """ test last name """
        user = self.test_class()
        self.assertIsInstance(user.last_name, str)

    def test_password(self):
        """ test password """
        user = self.test_class()
        self.assertIsInstance(user.password, str)
