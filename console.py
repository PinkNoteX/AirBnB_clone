#!/usr/bin/python3
""" the console """
import cmd
from models.base_model import BaseModel
from models.__init__ import storage
class HBNBCommand(cmd.Cmd):
    """ hbnbcommand class """
    prompt = '(hbnb) '
    classes = {"BaseModel": BaseModel}
    def do_EOF(self, command):
        """ EOF Handeling """
        print()
        exit()

    def help_EOF(self):
        """ EOF help """
        print('EOF command to exit the program\n')

    def emptyline(self):
        """ prevent empty lines """
        pass

    def do_quit(self, command):
        """ quit """
        exit()

    def help_quit(self):
        """ quit help """
        print('Quit command to exit the program\n')




if __name__ == '__main__':
    HBNBCommand().cmdloop()
