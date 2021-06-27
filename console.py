#!/usr/bin/python3
"""
This module contains the entry point of the command interpreter
"""
import cmd
from models.base_model import BaseModel
from models import storage

class HBNBCommand(cmd.Cmd):

    prompt = '(hbnb)'
    class_list = ["User", "BaseModel", "Place", "State", "City",
                "Amenity", "Review"]

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
        elif line not in HBNBCommand.class_list:
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
        if len(line) == 0:
            print("** class name missing **")
        elif arguments[0] not in HBNBCommand.class_list:
            print("** class doesn't exist **")
        elif len(arguments) < 2:
            print("** instance id missing **")
        else:
            key_name = arguments[0] + "." + arguments[1]
            obj = storage.find_key(key_name)
            print(obj)

    def do_destroy(self, line):
        """  """

        arguments = line.split(' ', 1)
        if len(line) == 0:
            print("** class name missing **")
        elif arguments[0] not in HBNBCommand.class_list:
            print("** class doesn't exist **")
        elif len(arguments) < 2:
            print("** instance id missing **")
        else:
            key_name = arguments[0] + "." + arguments[1]
            """no se si esto se pueda xd, de no ser asi hay que importar FileStorage"""
            obj = storage.find_key(key_name)
            if obj is not None:
                storage.FileStorage.__objects.del(key_name)
                storage.save()

    def do_all(self, line):
        """  """

        all_objs = storage.all()
        for obj_id in all_objs.keys():
            obj = all_objs[obj_id]
            print(obj)



    def emptyline(self):
        """an empty line + ENTER shouldn’t execute anything"""
        return


if __name__ == '__main__':
    HBNBCommand().cmdloop()
