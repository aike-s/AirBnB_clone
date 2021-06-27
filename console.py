#!/usr/bin/python3
""" that contains the entry point of the command interpreter"""
import cmd


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

    def emptyline(self):
        """an empty line + ENTER shouldn’t execute anything"""
        return


if __name__ == '__main__':
    HBNBCommand().cmdloop()
