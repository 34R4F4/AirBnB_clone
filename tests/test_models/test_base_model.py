#!/usr/bin/python3

import unittest
from datetime import datetime
from base_model import BaseModel  # base_model.py >> class BaseModel


class TestBaseModel(unittest.TestCase):
    def setUp(self):
        self.base_model = BaseModel()

    def test_id_generation(self):
        # Test if the id attribute is generated
        self.assertIsNotNone(self.base_model.id)

    def test_created_at(self):
        # Test if the created_at attribute is set to the current datetime
        self.assertIsInstance(self.base_model.created_at, datetime)

    def test_updated_at(self):
        # Test if the updated_at attribute is set to the current datetime
        self.assertIsInstance(self.base_model.updated_at, datetime)

    def test_updated_at_after_save(self):
        # Test if the updated_at attribute is updated after calling save()
        previous_updated_at = self.base_model.updated_at
        self.base_model.save()
        self.assertNotEqual(previous_updated_at, self.base_model.updated_at)

    def test_to_dict(self):
        # Test if to_dict() returns the expected dictionary
        expected_dict = {
            'id': self.base_model.id,
            'created_at': self.base_model.created_at.isoformat(),
            'updated_at': self.base_model.updated_at.isoformat(),
            '__class__': 'BaseModel'
        }
        self.assertDictEqual(expected_dict, self.base_model.to_dict())


if __name__ == '__main__':
    unittest.main()
