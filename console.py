#!/usr/bin/python3
"""
HBNB Command Module
"""

import cmd
import ast
import re
import json
from models.base_model import BaseModel
from models import storage
from models.user import User
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.state import State
from models.city import City


def split_curly_braces(e_arg):
    """
    Splits the curly braces for the update method
    """
    curly_braces = re.search(r"\{(.*?)\}", e_arg)

    if curly_braces:
        id_with_comma = shlex.split(e_arg[:curly_braces.span()[0]])
        id = [i.strip(",") for i in id_with_comma][0]

        str_data = curly_braces.group(1)
        try:
            arg_dict = ast.literal_eval("{" + str_data + "}")
        except Exception:
            print("**  invalid dictionary format **")
            return
        return id, arg_dict
    else:
        commands = e_arg.split(",")
        if commands:
            try:
                id = commands[0]
            except Exception:
                return "", ""
            try:
                attr_name = commands[1]
            except Exception:
                return id, ""
            try:
                attr_value = commands[2]
            except Exception:
                return id, attr_name
            return f"{id}", f"{attr_name} {attr_value}"

class HBNBCommand(cmd.Cmd):
    """
    HBNB command console class
    """
    prompt = "(hbnb) "
    classes = ["BaseModel", "User", "Amenity",
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
        elif arguments[0] not in self.classes:
            print("** class doesn't exist **")
        else:
            new = eval(f"{arguments[0]}()")
            my_obj = new.to_dict()
            with open("json_file", 'w') as file:
                json.dump(my_obj, file)
            print(new.id)

    def do_show(self, line):
        """Prints the string representation of an instance
        based on the class name and id"""

        arguments = line.split()
        print(arguments)
        if len(arguments) == 0:
            print("** class name missing **")
        elif arguments[0] not in self.classes:
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
        elif arguments[0] not in self.classes:
            print("** class doesn't exist **")
        elif len(arguments) < 2:
            print("** instance id missing **")
        else:
            objs = storage.all()

            key = "{}.{}".format(arguments[0], arguments[1])
            if key in objs:
                del objs[key]
            else:
                print("** no instance found **")

    def do_all(self, line):
        """
        Print the string representation of all
        instances or a specific class
        """
        objs = storage.all()
        arguments = line.split()

        if len(arguments) == 0:
            for key, value in objs.items():
                print(str(value))
        elif arguments[0] not in self.classes:
            print("** class doesn't exist **")
        else:
            for key, value in objs.items():
                print(str(value))

    def do_update(self, line):
        """Update an instance by adding or updating an attribute"""
        arguments = line.split()

        if len(arguments) == 0:
            print("** class name missing **")
        elif arguments[0] not in self.classes:
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
