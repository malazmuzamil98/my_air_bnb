#!/usr/bin/python3
"""Console, the command interpreter."""
import cmd
import sys
from models.base_model import BaseModel
from models import storage


class HBNBCommand(cmd.Cmd):
    """command interpeter"""

    prompt = "(hbnb) "
    classes = {
            "BaseModel": BaseModel
        }

    def do_create(self, arg):
        """creates new instance"""

        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name not in self.classes:
            print("** class doesn't exist **")
            return
        new_instance = self.classes[class_name]()
        new_instance.save()
        print(new_instance.id)

    def do_show(self, arg):
        """shows the string representation of an object"""

        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        class_name = args[0]

        if class_name not in self.classes:
            print("** class doesn't exist **")
            return

        elif len(args) < 2:
            print("** instance id missing **")
            return

        else:
            key = "{}.{}".format(args[0], args[1])
            if key in storage.all():
                obj = storage.all()[key]
                print(obj)
            else:
                print("** no instance found **")

    def do_destroy(self, arg):
        """destroies an object"""

        if not arg:
            print("** class name missing **")
            return

        args = arg.split()
        class_name = args[0]

        if class_name not in self.classes:
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        instance_id = args[1]
        key = class_name + "." + instance_id

        if key not in storage.all():
            print("** no instance found **")
            return

        del storage.all()[key]
        storage.save()

    def do_all(self, arg):
        """Prints all string representation of all instences"""

        args = arg.split()
        if args and args[0] not in self.classes:
            print("** class doesn't exist **")
            return

        instances = []
        for key, value in storage.all().items():
            class_name = key.split('.')[0]
            if not args or class_name == args[0]:
                instances.append(str(value))
        print(instances)

    def do_update(self, arg):
        """Updates an instance based on the class name"""

        if not arg:
            print("** class name missing **")
            return

        args = arg.split()
        class_name = args[0]

        if class_name not in self.classes:
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        instance_id = args[1]
        key = class_name + "." + instance_id

        if key not in storage.all():
            print("** no instance found **")
            return

        if len(args) < 3:
            print("** attribute name missing **")
            return

        if len(args) < 4:
            print("** value missing **")
            return

        attribute_name = args[2]
        attribute_value = args[3]
        instance = storage.all()[key]

        # Casting attribute value to the attribute type
        attribute_type = type(getattr(instance, attribute_name))
        try:
            if attribute_type is str:
                attribute_value = str(attribute_value)
            elif attribute_type is int:
                attribute_value = int(attribute_value)
            elif attribute_type is float:
                attribute_value = float(attribute_value)
        except ValueError:
            print("** value must be of type " + str(attribute_type) + " **")
            return

        setattr(instance, attribute_name, attribute_value)
        instance.save()

    def do_quit(self, arg):
        """Quit command to exit the program"""

        return True

    def emptyline(self):
        """empty input"""
        pass

    def do_EOF(self, arg):
        """handels EOF (CTRL+D) to exit the interpreter"""

        return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()
