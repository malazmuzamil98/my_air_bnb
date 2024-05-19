#!/usr/bin/env python3
"""
a unittest module for the place.py module
"""
import unittest
from models.place import Place
from models.__init__ import storage
from datetime import datetime as dt
import os
from json import load


class Test_Place(unittest.TestCase):
    """
    a testing class that inherits from unittest and
    implements methods for testing Place's methods
    and functionalities
    """

    def test_instantiate(self):
        """
        tests if instatiation is doe correctly
        """
        self.assertEqual(Place, type(Place()))

    def test_id_is_string(self):
        """
        tests if id is assigned correctly
        """
        self.assertEqual(str, type(Place().id))

    def test_created_at(self):
        """
        tests if crated_at is assigned correctly
        """
        self.assertEqual(dt, type(Place().created_at))

    def test_updated_at(self):
        """
        tests if updated_at is assigned correctly
        """
        self.assertEqual(dt, type(Place().updated_at))

    def test_city_id_exists(self):
        """
        tests if the self.city_id exists
        """
        x = Place()
        self.assertTrue(hasattr(x, "city_id"))
        self.assertEqual(str, type(x.city_id))

    def test_user_id_exists(self):
        """
        tests if the self.user_id exists
        """
        x = Place()
        self.assertTrue(hasattr(x, "user_id"))
        self.assertEqual(str, type(x.user_id))

    def test_name_exists(self):
        """
        tests if the self.name exists
        """
        x = Place()
        self.assertTrue(hasattr(x, "name"))
        self.assertEqual(str, type(x.name))

    def test_description_exists(self):
        """
        tests if the self.description exists
        """
        x = Place()
        self.assertTrue(hasattr(x, "description"))
        self.assertEqual(str, type(x.description))

    def test_number_rooms_exists(self):
        """
        tests if the self.number_rooms exists
        """
        x = Place()
        self.assertTrue(hasattr(x, "number_rooms"))
        self.assertEqual(int, type(x.number_rooms))

    def test_number_bathrooms_exists(self):
        """
        tests if the self.number_bathrooms exists
        """
        x = Place()
        self.assertTrue(hasattr(x, "number_bathrooms"))
        self.assertEqual(int, type(x.number_bathrooms))

    def test_max_guest_exists(self):
        """
        tests if the self.max_guest exists
        """
        x = Place()
        self.assertTrue(hasattr(x, "max_guest"))
        self.assertEqual(int, type(x.max_guest))

    def test_price_by_night_exists(self):
        """
        tests if the self.price_by_night exists
        """
        x = Place()
        self.assertTrue(hasattr(x, "price_by_night"))
        self.assertEqual(int, type(x.price_by_night))

    def test_latitude_exists(self):
        """
        tests if the self.latitude exists
        """
        x = Place()
        self.assertTrue(hasattr(x, "latitude"))
        self.assertEqual(float, type(x.latitude))

    def test_longitude_exists(self):
        """
        tests if the self.longitude exists
        """
        x = Place()
        self.assertTrue(hasattr(x, "longitude"))
        self.assertEqual(float, type(x.longitude))

    def test_amenity_ids_exists(self):
        """
        tests if the self.amenity_ids exists
        """
        x = Place()
        self.assertTrue(hasattr(x, "amenity_ids"))
        self.assertEqual(list, type(x.amenity_ids))

    def test_constructor_with_kwargs(self):
        """
        tests the constructor with a dictionary of
        values passed as a kwargs argument
        """
        date = dt.now().isoformat()
        a = {"id": "3456", "created_at": date, "updated_at": date}
        x = Place(**a)
        self.assertEqual(x.id, a["id"])
        self.assertEqual(x.created_at, dt.fromisoformat(a["created_at"]))
        self.assertEqual(x.updated_at, dt.fromisoformat(a["updated_at"]))

    def test_constructor_with_args(self):
        date = dt.now().isoformat()
        a = {"id": "3456", "created_at": date, "updated_at": date}
        x = Place(None, **a)
        self.assertNotIn(None, x.__dict__)

    def test_string_representation(self):
        """
        tests the string represenation of Place
        """
        self.assertEqual(str, type(str(Place())))

    def test_string_class_name(self):
        """
        tests if str has the correct class name
        """
        self.assertIn(
            f"[{Place().__class__.__name__}]", str(Place()))

    def test_string_id(self):
        """
        tests is str has the correct id
        """
        x = Place()
        self.assertIn(f"({x.id})", str(x))

    def test_string_dict(self):
        """
        tests if str has the correct dictioanry
        """
        x = Place()
        self.assertIn(f"{x.__dict__}", str(x))


class Test_dict(unittest.TestCase):
    """
    tests the self.to_dict() method
    """

    def test_dict(self):
        """
        tests the dictionary representation of Place
        """
        self.assertEqual(dict, type(Place().to_dict()))

    def test_to_dict_is_dict(self):
        """
        tests if the dictionary representation is __dict__
        """
        x = Place()
        self.assertIsNot(x.__dict__, x.to_dict())

    def test_class_attr_in_dict(self):
        """
        tests the __class__ attribute in the
        dictionary representation
        """
        x = Place()
        self.assertIn("__class__", x.to_dict())

    def test_created_at_attr_in_dict(self):
        """
        tests the created_at attribute in the
        dictionary representation
        """
        x = Place()
        self.assertIn("created_at", x.to_dict())

    def test_updated_at_attr_in_dict(self):
        """
        tests the updated_at attribute in the
        dictionary representation
        """
        x = Place()
        self.assertIn("updated_at", x.to_dict())

    def test_class_value_type(self):
        """
        tests __class__ value in the dictionary
        representation
        """
        x = Place()
        self.assertEqual(str, type(x.to_dict()["__class__"]))

    def test_class_value(self):
        """
        tests if __class__ has the correct value
        """
        x = Place()
        self.assertEqual(x.to_dict()["__class__"], f"{x.__class__.__name__}")

    def test_created_at_value(self):
        """
        tests created_at value in the dictionary
        representation
        """
        x = Place()
        self.assertEqual(str, type(x.to_dict()["created_at"]))

    def test_updated_at_value(self):
        """
        tests updated_at value in the dictionary
        representation
        """
        x = Place()
        self.assertEqual(str, type(x.to_dict()["updated_at"]))

    def test_instance_stored(self):
        """
        tests if ne instances are being stored
        """
        self.assertIn(Place().to_dict(), storage.all().values())

    def test_to_dict_with_argument(self):
        """
        tests .to_dict() with arguments
        """
        x = Place()
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
        x = Place()
        date = x.updated_at
        x.save()
        self.assertNotEqual(date, x.updated_at)

    def test_save_method_json_file(self):
        """
        tests saving to a JSON file
        """
        x = Place()
        x.save()
        lookup = f"{x.__class__.__name__}.{x.id}"
        with open("file.json") as f:
            y = load(f)
            self.assertIn(lookup, y.keys())

    def test_save_with_argument(self):
        """
        tests the .save() method with arguments
        """
        x = Place()
        with self.assertRaises(TypeError):
            x.save(None)