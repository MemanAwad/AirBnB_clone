#!/usr/bin/python3
"""
HBNB Command Module
"""

import cmd
import json
from models.base_model import BaseModel
from models import storage
from models.user import User
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.state import State
from models.city import City


class HBNBCommand(cmd.Cmd):
    """
    HBNB command console class
    """
    prompt = "(hbnb) "
    __classes = ["BaseModel", "User", "Amenity",
                 "Place", "Review", "State", "City"]

    def do_EOF(self, line):
        """Quit command to exit the program"""
        return True

    def do_quit(self, line):
        """Quit command to exit the program\n"""
        return True

    def emptyline(self):
        """function checks for empty line"""
        pass

    def do_create(self, line):
        """Creates a new instance of BaseModel, saves it and prints the id"""
        arguments = line.split()

        if len(arguments) == 0:
            print("** class name missing **")
        elif arguments[0] not in self.__classes:
            print("** class doesn't exist **")
        else:
            #cls = globals()[arguments[0]]
            #new_cls = cls()
            #storage.save()
            new_instance = eval(arguments[0])()
            new_instance.save()
            print(new_instance.id)

    def do_show(self, line):
        """Prints the string representation of an instance
        based on the class name and id"""

        arguments = line.split()
        if len(arguments) == 0:
            print("** class name missing **")
        elif arguments[0] not in self.__classes:
            print("** class doesn't exist **")
        elif len(arguments) < 2:
            print("** instance id missing **")
        else:
            objs = storage.all()

            key = "{}.{}".format(arguments[0], arguments[1])
            if key in objs:
                print(objs[key])
            else:
                print("** no instance found **")

    def do_destroy(self, line):
        """Delete an instance based on the class name and id"""
        arguments = line.split()
        if len(arguments) == 0:
            print("** class name missing **")
        elif arguments[0] not in self.__classes:
            print("** class doesn't exist **")
        elif len(arguments) < 2:
            print("** instance id missing **")
        else:
            objs = storage.all()

            key = "{}.{}".format(arguments[0], arguments[1])
            if key in objs:
                del objs[key]
                storage.save()
            else:
                print("** no instance found **")

    def do_all(self, line):
        """
        Print the string representation of all
        instances or a specific class
        """
        objj = []
        arg = line.split()

        if len(arg) > 0 and arg[0] not in self.__classes:
            print("** class doesn't exist **")
        else:
            objj = []
            for obj in storage.all().values():
                if len(arg) > 0 and arg[0] == obj.__class__.__name__:
                    objj.append(obj.__str__())
                elif len(arg) == 0:
                    objj.append(obj.__str__())
            print(objj)

    def do_update(self, line):
        """Update an instance by adding or updating an attribute"""
        arguments = line.split()

        if len(arguments) == 0:
            print("** class name missing **")
        elif arguments[0] not in self.__classes:
            print("** class doesn't exist **")
        elif len(arguments) < 2:
            print("** instance id missing **")
        else:
            objs = storage.all()

            key = "{}.{}".format(arguments[0], arguments[1])

            if key not in objs:
                print("** no instance found **")
            elif len(arguments) < 3:
                print("** attribute name missing **")
            elif len(arguments) < 4:
                print("** value missing **")
            else:
                obj = objs[key]
                attr_name = arguments[2]
                attr_value = arguments[3]

                try:
                    attr_value = eval(attr_value)
                except Exception:
                    pass
                setattr(obj, attr_name, attr_value)
                obj.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
