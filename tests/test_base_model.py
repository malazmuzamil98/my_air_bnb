#!/usr/bin/python3
"""BaseModel"""
from unittest.mock import patch
from datetime import datetime
import unittest
import sys
import uuid
from models.base_model import BaseModel
from datetime import datetime
from models import storage
import os
from json import load

sys.path.append('../')


class TestBaseModel(unittest.TestCase):
    """BaseModel"""

    def setUp(self):
        """BaseModel"""
        self.model = BaseModel()

    def tearDown(self):
        """BaseModel"""
        del self.model

    def test_init_no_kwargs(self):
        """BaseModel"""
        self.assertIsNotNone(self.model.id)
        self.assertTrue(isinstance(self.model.id, str))
        self.assertTrue(isinstance(self.model.created_at, datetime))
        self.assertTrue(isinstance(self.model.updated_at, datetime))
        self.assertEqual(self.model.created_at, self.model.updated_at)

    def test_init_with_kwargs(self):
        """BaseModel"""
        test_id = str(uuid.uuid4())
        test_time = datetime.now()
        test_kwargs = {
            'id': test_id,
            'created_at': test_time.isoformat(),
            'updated_at': test_time.isoformat(),
            '__class__': 'SomeClass'
        }
        model_with_kwargs = BaseModel(**test_kwargs)
        self.assertEqual(model_with_kwargs.id, test_id)
        self.assertEqual(model_with_kwargs.created_at, test_time)
        self.assertEqual(model_with_kwargs.updated_at, test_time)

    def test_str(self):
        """BaseModel"""
        expected_str_format = "[BaseModel] ({}) {}".format(
            self.model.id, self.model.__dict__)
        self.assertEqual(expected_str_format, str(self.model))

    @patch('models.storage')
    def test_save(self, mock_storage):
        """BaseModel"""
        previous_updated_at = self.model.updated_at
        self.model.save()
        self.assertGreater(self.model.updated_at, previous_updated_at)
        mock_storage.save.assert_called_once()

    def test_to_dict(self):
        """BaseModel"""
        model_dict = self.model.to_dict()
        expected_keys = {"id", "__class__", "created_at", "updated_at"}
        self.assertTrue(expected_keys.issubset(model_dict.keys()))
        self.assertEqual(model_dict["__class__"], "BaseModel")
        self.assertEqual(model_dict["created_at"],
                         self.model.created_at.isoformat())
        self.assertEqual(model_dict["updated_at"],
                         self.model.updated_at.isoformat())
        self.assertNotIn("_sa_instance_state", model_dict)

    def test_to_dict_with_extra_attribute(self):
        """BaseModel"""
        self.model.name = "Test Name"
        model_dict = self.model.to_dict()
        self.assertIn("name", model_dict)
        self.assertEqual(model_dict["name"], "Test Name")

class Test_dict(unittest.TestCase):
    """
    tests the self.to_dict() method
    """

    def test_dict(self):
        """
        tests the dictionary representation of BaseModel
        """
        self.assertEqual(dict, type(BaseModel().to_dict()))

    def test_to_dict_is_dict(self):
        """
        tests if the dictionary representation is __dict__
        """
        x = BaseModel()
        self.assertIsNot(x.__dict__, x.to_dict())

    def test_class_attr_in_dict(self):
        """
        tests the __class__ attribute in the
        dictionary representation
        """
        x = BaseModel()
        self.assertIn("__class__", x.to_dict())

    def test_created_at_attr_in_dict(self):
        """
        tests the created_at attribute in the
        dictionary representation
        """
        x = BaseModel()
        self.assertIn("created_at", x.to_dict())

    def test_updated_at_attr_in_dict(self):
        """
        tests the updated_at attribute in the
        dictionary representation
        """
        x = BaseModel()
        self.assertIn("updated_at", x.to_dict())

    def test_class_value_type(self):
        """
        tests __class__ value in the dictionary
        representation
        """
        x = BaseModel()
        self.assertEqual(str, type(x.to_dict()["__class__"]))

    def test_class_value(self):
        """
        tests if __class__ has the correct value
        """
        x = BaseModel()
        self.assertEqual(x.to_dict()["__class__"], f"{x.__class__.__name__}")

    def test_created_at_value(self):
        """
        tests created_at value in the dictionary
        representation
        """
        x = BaseModel()
        self.assertEqual(str, type(x.to_dict()["created_at"]))

    def test_updated_at_value(self):
        """
        tests updated_at value in the dictionary
        representation
        """
        x = BaseModel()
        self.assertEqual(str, type(x.to_dict()["updated_at"]))

    def test_instance_stored(self):
        """
        tests if ne instances are being stored
        """
        self.assertIn(BaseModel().to_dict(), storage.all().values())

    def test_to_dict_with_argument(self):
        """
        tests .to_dict() with arguments
        """
        x = BaseModel()
        with self.assertRaises(TypeError):
            x.to_dict(None)


class Tess_save(unittest.TestCase):
    """
    tests the .save() method
    """

    @classmethod
    def setUp(self):
        try:
            os.rename("file.json", "temp")
        except IOError:
            pass

    @classmethod
    def tearDown(self):
        try:
            os.remove("file.json")
        except IOError:
            pass
        try:
            os.rename("temp", "file.json")
        except IOError:
            pass

    def test_save_method_updated_at(self):
        """
        tests the .save() method
        """
        x = BaseModel()
        date = x.updated_at
        x.save()
        self.assertNotEqual(date, x.updated_at)

    def test_save_method_json_file(self):
        """
        tests saving to a JSON file
        """
        x = BaseModel()
        x.save()
        lookup = f"{x.__class__.__name__}.{x.id}"
        with open("file.json") as f:
            y = load(f)
            self.assertIn(lookup, y.keys())

    def test_save_with_argument(self):
        """
        tests the .save() method with arguments
        """
        x = BaseModel()
        with self.assertRaises(TypeError):
            x.save(None)

if __name__ == '__main__':
    unittest.main()
