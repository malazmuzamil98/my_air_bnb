#!/usr/bin/python3
"""Console, the command interpreter."""
import cmd
import re
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.review import Review
from models.amenity import Amenity
from models import storage


class HBNBCommand(cmd.Cmd):
    """command interpeter"""

    prompt = "(hbnb) "
    # classes = {"BaseModel": BaseModel,
    #            "User": User,
    #            "State": State,
    #            "City": City,
    #            "Place": Place,
    #            "Review": Review,
    #            "Amenity": Amenity
    #         }
    classes = storage.class_dict()
    objects = storage.all()
    storage.reload()

    def default(self, line):
        """Handles the default commands"""

        args = line.split('(')
        if len(args) != 2:
            print("** invalid command **")
            return

        cmd_args = args[1].split(')')[0]
        cmd_name = args[0].strip()

        if not cmd_args:
            print("** invalid command **")
            return

        class_name, action = cmd_name.split('.')

        if class_name not in self.classes:
            print("** class doesn't exist **")
            return

        instance_id = None
        update_dict = None

        if action == 'show':
            instance_id = cmd_args.strip().strip('"')
            self.do_show(f"{class_name} {instance_id}")

        elif action == 'destroy':
            instance_id = cmd_args.strip().strip('"')
            self.do_destroy(f"{class_name} {instance_id}")

        elif action == 'update':
            cmd_args = cmd_args.split(',', 1)
            if len(cmd_args) != 2:
                print("** invalid command **")
                return
            instance_id = cmd_args[0].strip().strip('"')
            update_dict = eval(cmd_args[1].strip())
            self.do_update(f"{class_name} {instance_id}", update_dict)

        else:
            print("** invalid command **")

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

    def do_count(self, line):
        """Retrieve the number of instances of a class"""
        args = line.split()
        if len(args) == 1:
            class_name = args[0]
            if class_name in self.classes:
                count = sum(
                    1 for obj in storage.all().values()
                    if isinstance(obj, eval(class_name)))
                print(count)
            else:
                print("** class doesn't exist **")
        else:
            print("** invalid command **")

    def parseline(self, line):
        """Parse the line to handle <class name>.all()
        and <class name>.count()"""
        orig_line = line
        line = line.strip()
        class_name = None
        command = None

        match = re.match(r'^(\w+)\.(all|count)\(\)$', line)
        if match:
            class_name = match.group(1)
            command = match.group(2)
            return command, class_name, orig_line

        return cmd.Cmd.parseline(self, orig_line)

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
