#!/usr/bin/python3
""" review unittest """
from models.review import Review
from tests.test_models.test_base_model import TestBaseModel


class TestReview(TestBaseModel):
    """ review test """
    def __init__(self, *args, **kwargs):
        """ init """
        super().__init__(*args, **kwargs)
        self.test_class = Review
        self.test_name = "Review"

    def test_place_id(self):
        """ test place id """
        review = self.test_class()
        self.assertIsInstance(review.place_id, str)

    def test_user_id_review(self):
        """ test user id """
        review = self.test_class()
        self.assertIsInstance(review.user_id, str)

    def test_text(self):
        """ test text """
        review = self.test_class()
        self.assertIsInstance(review.text, str)
