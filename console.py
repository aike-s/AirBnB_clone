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

    def print_error(self, *line):
        """ Verify errors in line parameter """
        """ Returns False and prints error in case of error """
        """ or returns True in case of non error """
        """ esto es una prueba :) """



        if line[0] is None:
            print("** class name missing **")
            return False
        elif line[0] not in self.class_list:
            print("** class doesn't exist **")
            return False
        elif line[1] == True:
            arguments = line[0].split(' ', 1)
            if len(arguments) < 2:
                print("** instance id missing **")
                return False
        else:
            return True

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
        """ Create and save a new instance """
        """ aqui estoy probando la funcion print_error, se supone """
        """ que se imprime el error desde la funcion y en caso de no haber error """
        """ (o sea que retorne True), se crea la instancia """
        if len(line) == 0:
            print("** class name missing **")
        elif line != "BaseModel":
            print("** class doesn't exist **")
        else:
            new_obj = BaseModel()
            new_obj.save()
            print(new_obj.id)


    def do_show(self, line):
        """ Prints the string representation of an instance """
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
        """ Deletes an instance """

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
            if obj is not None:
                storage.all().pop(key_name)
                storage.save()

    def do_all(self, line):
        """ Prints all string representation of all instances """
        arguments = line.split(' ', 1)
        if len(line) == 0 or arguments[0] == 'BaseModel':
            all_objs = storage.all()
            for obj_id in all_objs.keys():
                obj = all_objs[obj_id]
                print(obj)
        elif line in HBNBCommand.class_list:
            """ retornar e imprimir solo las instancias de esta clase en especifico """

        else:
            print("** class doesn't exist **")

    def emptyline(self):
        """an empty line + ENTER shouldn’t execute anything"""
        return


if __name__ == '__main__':
    HBNBCommand().cmdloop()
