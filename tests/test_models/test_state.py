#!/usr/bin/python3
""" state unittest """
from models.state import State
from tests.test_models.test_base_model import TestBaseModel


class TestState(TestBaseModel):
    """ state test """
    def __init__(self, *args, **kwargs):
        """ init """
        super().__init__(*args, **kwargs)
        self.test_class = State
        self.test_name = "State"

    def test_state_id(self):
        """ test id """
        state = self.test_class()
        self.assertIsInstance(state.name, str)
