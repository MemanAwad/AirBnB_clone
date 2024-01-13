import cmd
import json
from models.base_model import BaseModel

class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "

    def do_EOF(self, line):
        """Quit command to exit the program"""
        return True

    def do_quit(self, line):
        """Quit command to exit the program\n"""
        return True

    def emptyline(self):
        """function checks for empty line"""
        return
    
    def do_create(self,line):
        """Creates a new instance of BaseModel, saves it and prints the id"""
        if len(line) < 2:
            print("** class name missing **")
        elif line != 'BaseModel':
            print("** class doesn't exist **")
        else:
            new = BaseModel()
            my_obj = new.to_dict()
            with open("json_file", 'w') as file:
                json.dump(my_obj, file)
            print(new.id)

    def do_show(self, line):
        """Prints the string representation of an instance
        based on the class name and id"""

        if len(line) < 2:
            print("** class name missing **")
        elif line[1] != "BaseModel":
            print("** class doesn't exist **")
        elif line[0] == "BaseModel" and len(line) < 3:
            print("** instance id missing **")
        else:
            print("All GOOD!")
            

if __name__ == '__main__':
    HBNBCommand().cmdloop()
