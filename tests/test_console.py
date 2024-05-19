#!/usr/bin/env python3
"""
this module is meant to test the console.py. it tests the
command line commands to check is their
output is correct or not
"""
import unittest
from unittest.mock import patch
from io import StringIO
from console import HBNBCommand
from models import storage
from os import rename, remove
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


class TestConsoleCommands_help(unittest.TestCase):
    """
    a class that tests the help command
    """

    def setUp(self):
        try:
            rename("file.json", "temp")
        except IOError:
            pass

    def tearDown(self):
        try:
            remove("file.json")
        except IOError:
            pass
        try:
            rename("temp", "file.json")
        except IOError:
            pass

    def test_help(self):
        """
        tests the help command
        """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help")
            c_output = """Documented commands (type help <topic>):
========================================
EOF  all  create  destroy  help  quit  show  update"""
            output = f.getvalue().strip()
            self.assertIn(c_output, output)

    def test_help_quit(self):
        """
        tests the help quit command
        """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help quit")
            c_output = "Quit command to exit the program"
            output = f.getvalue().strip()
            self.assertIn(c_output, output)

    def test_help_eof(self):
        """
        Tests the help command for EOF.
        """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help EOF")
            c_output = "executes when quitting the console"
            output = f.getvalue().strip()
            self.assertIn(c_output, output)

    def test_help_help(self):
        """
        tests the help help command
        """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help help")
            c_output = 'List available commands with "help" \
or detailed help with "help cmd".'
            output = f.getvalue().strip()
            self.assertIn(c_output, output)

    def test_help_all(self):
        """
        tests the help all command
        """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help all")
            c_output = """Prints all string representation of all instances
        based or not on the class name. Ex: $ all
        BaseModel or $ all"""
            output = f.getvalue().strip()
            self.assertIn(c_output, output)

    def test_help_show(self):
        """
        tests the help show command
        """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help show")
            c_output = """Prints the string representation of an instance
        based on the class name and id

        Args:
            args: user input"""
            output = f.getvalue().strip()
            self.assertIn(c_output, output)

    def test_help_create(self):
        """
        tests the help create command
        """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help create")
            c_output = """Creates a new instance of the given class object ,
        saves it (to the JSON file) and prints the id

        Args:
            arg: user input (class name)"""
            output = f.getvalue().strip()
            self.assertIn(c_output, output)

    def test_help_update(self):
        """
        tests the help update command
        """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help update")
            c_output = """Updates an instance based on the class name
        and id by adding or updating attribute (save
        the change into the JSON file)

        Args:
            arg: user input"""
            output = f.getvalue().strip()
            self.assertIn(c_output, output)

    def test_help_destroy(self):
        """
        tests the help destroy command
        """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help destroy")
            c_output = """Deletes an instance based on the class
        name and id (save the change into the JSON file"""
            output = f.getvalue().strip()
            self.assertIn(c_output, output)


class TestConsoleCommands_create(unittest.TestCase):
    """
    class that tests the create command
    """

    def setUp(self):
        try:
            rename("file.json", "temp")
        except IOError:
            pass

    def tearDown(self):
        try:
            remove("file.json")
        except IOError:
            pass
        try:
            rename("temp", "file.json")
        except IOError:
            pass

    def test_create_instance(self):
        """
        tests the create command
        """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create")
            output = f.getvalue().strip()
            self.assertIn("** class name missing **", output)

    def test_create_instance_with_class_name(self):
        """
        tests the create command with an invalid
        class name
        """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create MyClass")
            output = f.getvalue().strip()
            self.assertIn("** class doesn't exist **", output)

    def test_create_instance_with_existing_class(self):
        """
        tests the create command with only a class name
        """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create BaseModel")
            output = f.getvalue().strip()
            _dict = storage.all().keys()
            text = f"BaseModel.{output}"
            self.assertIn(text, _dict)

    def test_create_instance_with_Amenity_class(self):
        """
        tests the create command with only a class name
        """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create Amenity")
            output = f.getvalue().strip()
            _dict = storage.all().keys()
            text = f"Amenity.{output}"
            self.assertIn(text, _dict)

    def test_create_instance_with_City_class(self):
        """
        tests the create command with only a class name
        """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create City")
            output = f.getvalue().strip()
            _dict = storage.all().keys()
            text = f"City.{output}"
            self.assertIn(text, _dict)

    def test_create_instance_with_PLace_class(self):
        """
        tests the create command with only a class name
        """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create Place")
            output = f.getvalue().strip()
            _dict = storage.all().keys()
            text = f"Place.{output}"
            self.assertIn(text, _dict)

    def test_create_instance_with_Review_class(self):
        """
        tests the create command with only a class name
        """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create Review")
            output = f.getvalue().strip()
            _dict = storage.all().keys()
            text = f"Review.{output}"
            self.assertIn(text, _dict)

    def test_create_instance_with_State_class(self):
        """
        tests the create command with only a class name
        """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create State")
            output = f.getvalue().strip()
            _dict = storage.all().keys()
            text = f"State.{output}"
            self.assertIn(text, _dict)

    def test_create_instance_with_User_class(self):
        """
        tests the create command with only a class name
        """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create User")
            output = f.getvalue().strip()
            _dict = storage.all().keys()
            text = f"User.{output}"
            self.assertIn(text, _dict)


class TestConsoleCommands_all(unittest.TestCase):
    """
    class that tests the all command
    """

    def setUp(self):
        try:
            rename("file.json", "temp")
        except IOError:
            pass

    def tearDown(self):
        try:
            remove("file.json")
        except IOError:
            pass
        try:
            rename("temp", "file.json")
        except IOError:
            pass

    def test_all_instances(self):
        """
        tests the all command
        """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("all")
            output = f.getvalue().strip()
            a = [str(BaseModel(**value))
                 for key, value in storage.all().items() if "BaseModel" in key]
            b = [str(User(**value))
                 for key, value in storage.all().items() if "User" in key]
            c = [str(City(**value))
                 for key, value in storage.all().items() if "City" in key]
            d = [str(State(**value))
                 for key, value in storage.all().items() if "State" in key]
            e = [str(Place(**value))
                 for key, value in storage.all().items() if "Place" in key]
            f = [str(Review(**value))
                 for key, value in storage.all().items() if "Review" in key]
            g = [str(Amenity(**value))
                 for key, value in storage.all().items() if "Amenity" in key]
            z = [*a, *b, *c, *d, *e, *f, *g]
            self.assertEqual(str(z), output)

    def test_all_instances_with_base_model_class(self):
        """
        tests the all + a valid class name
        """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("all BaseModel")
            x = [str(BaseModel(**value))
                 for key, value in storage.all().items()
                 if "BaseModel" in key]
            output = f.getvalue().strip()
            self.assertEqual(str(x), output)

    def test_all_instances_with_my_class(self):
        """
        tests the all + an invalid class name
        """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("all MyClass")
            output = f.getvalue().strip()
            self.assertIn("** class doesn't exist **", output)


class TestConsoleCommands_show(unittest.TestCase):
    """
    class that tests the show command
    """

    def setUp(self):
        try:
            rename("file.json", "temp")
        except IOError:
            pass

    def tearDown(self):
        try:
            remove("file.json")
        except IOError:
            pass
        try:
            rename("temp", "file.json")
        except IOError:
            pass

    def test_show_instance(self):
        """
        tests the show command with no arguments
        """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("show")
            output = f.getvalue().strip()
            self.assertIn("** class name missing **", output)

    def test_show_instance_with_class_name(self):
        """
        tests the show command with an invalid
        class name
        """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("show MyClass")
            output = f.getvalue().strip()
            self.assertIn("** class doesn't exist **", output)

    def test_show_instance_with_existing_class(self):
        """
        tests the show command with a valid class name
        """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("show BaseModel")
            output = f.getvalue().strip()
            self.assertIn("** instance id missing **", output)

    def test_show_instance_with_right_id(self):
        """
        tests the show command with all arguments correct
        """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create BaseModel")
            _id = f.getvalue().strip()
            HBNBCommand().onecmd(f"show BaseModel {_id}")
            x = storage.all()
            _key = f"BaseModel.{_id}"
            for key, value in x.items():
                if key == _key and "BaseModel" in key:
                    y = BaseModel(**value)
            output = f.getvalue().strip()
            self.assertIn(str(y), output)

    def test_show_instance_with_wrong_id(self):
        """
        tests the show command with an invalid id
        """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("show BaseModel wrong_id")
            output = f.getvalue().strip()
            self.assertIn("** no instance found **", output)


class TestConsoleCommands(unittest.TestCase):
    """
    class that tests the destroy command
    """

    def setUp(self):
        try:
            rename("file.json", "temp")
        except IOError:
            pass

    def tearDown(self):
        try:
            remove("file.json")
        except IOError:
            pass
        try:
            rename("temp", "file.json")
        except IOError:
            pass

    def test_destroy_instance(self):
        """
        tests the destroy command without arguments
        """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("destroy")
            output = f.getvalue().strip()
            self.assertIn("** class name missing **", output)

    def test_destroy_instance_with_class_name(self):
        """
        tests the destroy command with an invalid
        class name
        """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("destroy MyClass")
            output = f.getvalue().strip()
            self.assertIn("** class doesn't exist **", output)

    def test_destroy_instance_with_existing_class(self):
        """
        tests the destroy command with a valid class name
        """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("destroy BaseModel")
            output = f.getvalue().strip()
            self.assertIn("** instance id missing **", output)

    def test_destroy_instance_with_right_id(self):
        """
        tests the destroy command with all correct arguments
        """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create BaseModel")
            _id = f.getvalue().strip()
            HBNBCommand().onecmd(f"destroy BaseModel {_id}")
            output = f.getvalue().strip()
            self.assertIn("", output)
            x = storage.all().keys()
            self.assertNotIn(f"BaseModel.{_id}", x)

    def test_destroy_instance_with_wrong_id(self):
        """
        tests the destroy command with an invalid id
        """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("destroy BaseModel wrong_id")
            output = f.getvalue().strip()
            self.assertIn("** no instance found **", output)


class TestConsoleCommands(unittest.TestCase):
    """
    class that tests the update command
    """

    def setUp(self):
        try:
            rename("file.json", "temp")
        except IOError:
            pass

    def tearDown(self):
        try:
            remove("file.json")
        except IOError:
            pass
        try:
            rename("temp", "file.json")
        except IOError:
            pass

    def test_update_instance(self):
        """
        tests the update command without arguments
        """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("update")
            output = f.getvalue().strip()
            self.assertIn("** class name missing **", output)

    def test_update_instance_with_class_name(self):
        """
        tests the command update command with an
        invalid class name
        """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("update MyClass")
            output = f.getvalue().strip()
            self.assertIn("** class doesn't exist **", output)

    def test_update_instance_with_existing_class(self):
        """
        tests the update command with only a valid
        class name
        """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("update BaseModel")
            output = f.getvalue().strip()
            self.assertIn("** instance id missing **", output)

    def test_update_instance_with_id(self):
        """
        tests the update command without a name
        """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create BaseModel")
            _id = f.getvalue().strip()
            HBNBCommand().onecmd(f"update BaseModel {_id}")
            output = f.getvalue().strip()
            self.assertIn("** attribute name missing **", output)

    def test_update_instance_with_id_and_attr(self):
        """
        tests the update command without the value
        """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create BaseModel")
            _id = f.getvalue().strip()
            HBNBCommand().onecmd(f"update BaseModel {_id} name")
            output = f.getvalue().strip()
            self.assertIn("** value missing **", output)

    def test_update_instance_with_id_attr_and_value(self):
        """
        tests the update command with all correct arguments
        """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create BaseModel")
            _id = f.getvalue().strip()
            HBNBCommand().onecmd(f"update BaseModel {_id} name value")
            output = f.getvalue().strip()
            self.assertIn("", output)
            x = storage.all()
            x[f"BaseModel.{_id}"]["name"] = "value"

    def test_update_instance_with_wrong_id(self):
        """
        tests the update command with an invalid id
        """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("update BaseModel wrong_id name value")
            output = f.getvalue().strip()
            self.assertIn("** no instance found **", output)


class TestConsoleCommands_dot_all(unittest.TestCase):
    """
    class that tests the .all() command
    """

    def setUp(self):
        try:
            rename("file.json", "temp")
        except IOError:
            pass

    def tearDown(self):
        try:
            remove("file.json")
        except IOError:
            pass
        try:
            rename("temp", "file.json")
        except IOError:
            pass

    def test_dot_all_instances_with_class_name(self):
        """
        tests the .all() command with an
        invalid class name
        """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("MyClass.all()")
            output = f.getvalue().strip()
            self.assertIn("** class doesn't exist **", output)

    def test_dot_all_instances_with_existing_class(self):
        """
        tests the .all() command with a valid
        class name
        """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("BaseModel.all()")
            x = [str(BaseModel(**value))
                 for key, value in storage.all().items()
                 if "BaseModel" in key]
            output = f.getvalue().strip()
            self.assertEqual(str(x), output)


class TestConsoleCommands_dot_show(unittest.TestCase):
    """
    class that tests the .show() command
    """

    def setUp(self):
        try:
            rename("file.json", "temp")
        except IOError:
            pass

    def tearDown(self):
        try:
            remove("file.json")
        except IOError:
            pass
        try:
            rename("temp", "file.json")
        except IOError:
            pass

    def test_dot_show_instance_with_invalid_class_name(self):
        """
        tests the .show() command with an invalid
        class name
        """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("MyClass.show()")
            output = f.getvalue().strip()
            self.assertIn("** class doesn't exist **", output)

    def test_dot_show_instance_with_existing_class(self):
        """
        tests the .show() command without id
        """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("BaseModel.show()")
            output = f.getvalue().strip()
            self.assertIn("** instance id missing **", output)

    def test_dot_show_instance_with_right_id(self):
        """
        tests the .show() command with correct arguments
        """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create BaseModel")
            _id = f.getvalue().strip()
            HBNBCommand().onecmd(f"BaseModel.show({_id})")
            x = storage.all()
            _key = f"BaseModel.{_id}"
            for key, value in x.items():
                if key == _key and "BaseModel" in key:
                    y = BaseModel(**value)
            output = f.getvalue().strip()
            self.assertIn(str(y), output)

    def test_dot_show_instance_with_wrong_id(self):
        """
        tests the .show() command with an invalid id
        """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("BaseModel.show(wrong_id)")
            output = f.getvalue().strip()
            self.assertIn("** no instance found **", output)


class TestConsoleCommands_dot_destroy(unittest.TestCase):
    """
    class that tests the .destroy() command
    """

    def setUp(self):
        try:
            rename("file.json", "temp")
        except IOError:
            pass

    def tearDown(self):
        try:
            remove("file.json")
        except IOError:
            pass
        try:
            rename("temp", "file.json")
        except IOError:
            pass

    def test_dot_destroy_instance_with_invalid_class_name(self):
        """
        tests the .destroy() command wit an invalid
        class name
        """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("(MyClass).destroy()")
            output = f.getvalue().strip()
            self.assertIn("** class doesn't exist **", output)

    def test_dot_destroy_instance_with_existing_class(self):
        """
        tests the .destroy() command without an id
        """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("BaseModel.destroy()")
            output = f.getvalue().strip()
            self.assertIn("** instance id missing **", output)

    def test_dot_destroy_instance_with_right_id(self):
        """
        tests the .destroy command with the correct argument
        """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create BaseModel")
            _id = f.getvalue().strip()
            HBNBCommand().onecmd(f"BaseModel.destroy({_id})")
            output = f.getvalue().strip()
            self.assertIn("", output)
            x = storage.all().keys()
            self.assertNotIn(f"BaseModel.{_id}", x)

    def test_dot_destroy_instance_with_wrong_id(self):
        """
        tests the .destroy() command with an invalid id
        """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("BaseModel.destroy(wrong_id)")
            output = f.getvalue().strip()
            self.assertIn("** no instance found **", output)


class TestConsoleCommands_dot_update(unittest.TestCase):
    """
    class that tests the .update() command
    """

    def setUp(self):
        try:
            rename("file.json", "temp")
        except IOError:
            pass

    def tearDown(self):
        try:
            remove("file.json")
        except IOError:
            pass
        try:
            rename("temp", "file.json")
        except IOError:
            pass

    def test_dot_update_instance_with_invalid_class_name(self):
        """
        tests the .update() command with an invalid
        class name
        """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("MyClass.update()")
            output = f.getvalue().strip()
            self.assertIn("** class doesn't exist **", output)

    def test_dot_update_instance_with_existing_class(self):
        """
        tests the .update() command without arguments
        """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("BaseModel.update()")
            output = f.getvalue().strip()
            self.assertIn("** instance id missing **", output)

    def test_dot_update_instance_with_id(self):
        """
        tests the .update() command without name, value
        """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create BaseModel")
            _id = f.getvalue().strip()
            HBNBCommand().onecmd(f"BaseModel.update({_id})")
            output = f.getvalue().strip()
            self.assertIn("** attribute name missing **", output)

    def test_dot_update_instance_with_id_and_name(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create BaseModel")
            _id = f.getvalue().strip()
            HBNBCommand().onecmd(f"BaseModel.update({_id}, name)")
            output = f.getvalue().strip()
            self.assertIn("** value missing **", output)

    def test_dot_update_instance_with_id_name_and_value(self):
        """
        tests the .update() command with all correct arguments
        """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create BaseModel")
            _id = f.getvalue().strip()
            HBNBCommand().onecmd(f"BaseModel.update({_id}, name, value)")
            output = f.getvalue().strip()
            self.assertIn("", output)
            x = storage.all()
            x[f"BaseModel.{_id}"]["name"] = "value"

    def test_dot_update_instance_with_wrong_id(self):
        """
        tests the .update() command with a wrong id
        """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("BaseModel.update(wrong id, name, value)")
            output = f.getvalue().strip()
            self.assertIn("** no instance found **", output)

    def test_dot_update_instance_with_id_dict(self):
        """
        tests the .update() command with a dictionary
        """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create BaseModel")
            _id = f.getvalue().strip()
            HBNBCommand().onecmd(f"BaseModel.update({_id}, "
                                 + "{'name': 'value'})")
            output = f.getvalue().strip()
            self.assertIn("", output)
            x = storage.all()
            x[f"BaseModel.{_id}"]["name"] = "value"

    def test_dot_update_instance_with_empty_dict(self):
        """
        tests the .update() command with an empty dictonary
        """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create BaseModel")
            _id = f.getvalue().strip()
            HBNBCommand().onecmd(f"BaseModel.update({_id}, ""{})")
            output = f.getvalue().strip()
            self.assertIn("** value missing **", output)

    def test_dot_update_instance_with_invalid_dict(self):
        """
        tests the .update() command with a dictonary
        missing a value
        """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create BaseModel")
            _id = f.getvalue().strip()
            HBNBCommand().onecmd(f"BaseModel.update({_id}, ""{name:})")
            output = f.getvalue().strip()
            self.assertIn("** value missing **", output)