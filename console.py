#!/usr/bin/python3
"""
This module contains the entry point of the command interpreter
"""
import cmd
from models.base_model import BaseModel
from models import storage

class HBNBCommand(cmd.Cmd):

    prompt = '(hbnb)'

    def do_EOF(self, line):
        """Quit command to exit the program \n"""
        try:
            return True
        except:
            print()

    def do_quit(self, line):
        """Quit command to exit the program \n"""
        try:
            return True
        except:
            print()

    def do_create(self, line):
        """  """

        if line is None:
            print("** class name missing **")
        elif line != "BaseModel":
            print("** class doesn't exist **")
        else:
            new_obj = BaseModel()
            new_obj.save()
            print(new_obj.id)

    def do_show(self, line):
        """  """
        """IMPORTANTE"""
        """ pensar en que pasa si envian mas parametros de lo debido"""

        arguments = line.split(' ', 1)
        if line is None:
            print("** class name missing **")
        elif arguments[0] != "BaseModel":
            print("** class doesn't exist **")
        elif len(arguments) < 2:
            print("** instance id missing **")
        else:
            name_key = arguments[0] + "." + arguments[1]
            all_objs = storage.all()


    def emptyline(self):
        """an empty line + ENTER shouldn’t execute anything"""
        return


if __name__ == '__main__':
    HBNBCommand().cmdloop()
