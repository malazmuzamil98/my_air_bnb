#!/usr/bin/env python3
"""
a unittest module for the user.py module
"""
import unittest
from models.user import User
from models import storage
from datetime import datetime as dt
import os
from json import load


class Test_User(unittest.TestCase):
    """
    a testing class that inherits from unittest and
    implements methods for testing User's methods
    and functionalities
    """

    def test_instantiate(self):
        """
        tests if instatiation is doe correctly
        """
        self.assertEqual(User, type(User()))

    def test_id_is_string(self):
        """
        tests if id is assigned correctly
        """
        self.assertEqual(str, type(User().id))

    def test_created_at(self):
        """
        tests if crated_at is assigned correctly
        """
        self.assertEqual(dt, type(User().created_at))

    def test_updated_at(self):
        """
        tests if updated_at is assigned correctly
        """
        self.assertEqual(dt, type(User().updated_at))

    def test_email_exist(self):
        """
        tests if the attribute self.email exists
        """
        x = User()
        self.assertTrue(hasattr(x, "email"))
        self.assertEqual(str, type(x.email))

    def test_password_exist(self):
        """
        tests if the attribute self.email exists
        """
        x = User()
        self.assertTrue(hasattr(x, "password"))
        self.assertEqual(str, type(x.password))

    def test_first_name_exist(self):
        """
        tests if the attribute self.email exists
        """
        x = User()
        self.assertTrue(hasattr(x, "first_name"))
        self.assertEqual(str, type(x.first_name))

    def test_last_name_exist(self):
        """
        tests if the attribute self.email exists
        """
        x = User()
        self.assertTrue(hasattr(x, "last_name"))
        self.assertEqual(str, type(x.last_name))

    def test_constructor_with_kwargs(self):
        """
        tests the constructor with a dictionary of
        values passed as a kwargs argument
        """
        date = dt.now().isoformat()
        a = {"id": "3456", "created_at": date, "updated_at": date}
        x = User(**a)
        self.assertEqual(x.id, a["id"])
        self.assertEqual(x.created_at, dt.fromisoformat(a["created_at"]))
        self.assertEqual(x.updated_at, dt.fromisoformat(a["updated_at"]))

    def test_constructor_with_args(self):
        date = dt.now().isoformat()
        a = {"id": "3456", "created_at": date, "updated_at": date}
        x = User(None, **a)
        self.assertNotIn(None, x.__dict__)

    def test_string_representation(self):
        """
        tests the string represenation of User
        """
        self.assertEqual(str, type(str(User())))

    def test_string_class_name(self):
        """
        tests if str has the correct class name
        """
        self.assertIn(
            f"[{User().__class__.__name__}]", str(User()))

    def test_string_id(self):
        """
        tests is str has the correct id
        """
        x = User()
        self.assertIn(f"({x.id})", str(x))

    def test_string_dict(self):
        """
        tests if str has the correct dictioanry
        """
        x = User()
        self.assertIn(f"{x.__dict__}", str(x))


class Test_dict(unittest.TestCase):
    """
    tests the self.to_dict() method
    """

    def test_dict(self):
        """
        tests the dictionary representation of User
        """
        self.assertEqual(dict, type(User().to_dict()))

    def test_to_dict_is_dict(self):
        """
        tests if the dictionary representation is __dict__
        """
        x = User()
        self.assertIsNot(x.__dict__, x.to_dict())

    def test_class_attr_in_dict(self):
        """
        tests the __class__ attribute in the
        dictionary representation
        """
        x = User()
        self.assertIn("__class__", x.to_dict())

    def test_created_at_attr_in_dict(self):
        """
        tests the created_at attribute in the
        dictionary representation
        """
        x = User()
        self.assertIn("created_at", x.to_dict())

    def test_updated_at_attr_in_dict(self):
        """
        tests the updated_at attribute in the
        dictionary representation
        """
        x = User()
        self.assertIn("updated_at", x.to_dict())

    def test_class_value_type(self):
        """
        tests __class__ value in the dictionary
        representation
        """
        x = User()
        self.assertEqual(str, type(x.to_dict()["__class__"]))

    def test_class_value(self):
        """
        tests if __class__ has the correct value
        """
        x = User()
        self.assertEqual(x.to_dict()["__class__"], f"{x.__class__.__name__}")

    def test_created_at_value(self):
        """
        tests created_at value in the dictionary
        representation
        """
        x = User()
        self.assertEqual(str, type(x.to_dict()["created_at"]))

    def test_updated_at_value(self):
        """
        tests updated_at value in the dictionary
        representation
        """
        x = User()
        self.assertEqual(str, type(x.to_dict()["updated_at"]))

    def test_instance_stored(self):
        """
        tests if ne instances are being stored
        """
        self.assertIn(User().to_dict(), storage.all().values())

    def test_to_dict_with_argument(self):
        """
        tests .to_dict() with arguments
        """
        x = User()
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
        x = User()
        date = x.updated_at
        x.save()
        self.assertNotEqual(date, x.updated_at)

    def test_save_method_json_file(self):
        """
        tests saving to a JSON file
        """
        x = User()
        x.save()
        lookup = f"{x.__class__.__name__}.{x.id}"
        with open("file.json") as f:
            y = load(f)
            self.assertIn(lookup, y.keys())

    def test_save_with_argument(self):
        """
        tests the .save() method with arguments
        """
        x = User()
        with self.assertRaises(TypeError):
            x.save(None)