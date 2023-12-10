#!/usr/bin/python3
""" the console """
import cmd
from models.base_model import BaseModel
from models.__init__ import storage
from models.user import User
from models.place import Place
from models.city import City
from models.amenity import Amenity
from models.state import State
from models.review import Review


Class_Dict = {"BaseModel": BaseModel,
              "User": User,
              "Place": Place,
              "City": City,
              "Amenity": Amenity,
              "State": State,
              "Review": Review}


class HBNBCommand(cmd.Cmd):
    """ hbnbcommand class """
    prompt = '(hbnb) '
    classes = {"BaseModel": BaseModel,
               "User": User,
               "Place": Place,
               "City": City,
               "Amenity": Amenity,
               "State": State,
               "Review": Review}

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

    def do_create(self, args):
        """ create new basemodel instance """
        if not args:
            print('** class name missing **')
            return
        elif args in Class_Dict:
            for key, value in Class_Dict.items():
                if key == args:
                    new_instance = Class_Dict[key]()
            storage.save()
            print(new_instance.id)
        else:
            print("** class doesn't exist **")

    def help_create(self):
        """ create help """
        print('Create command to create new instance\n')

    def help_show(self):
        """ show help"""
        print('Show command to show string representation\n')

    def do_show(self, args):
        """ print str """
        new_instance = args.partition(' ')
        class_name = new_instance[0]
        class_id = new_instance[2]
        if not args:
            print('** class name missing **')
            return
        if class_name not in Class_Dict:
            print("** class doesn't exist **")
            return
        if not class_id:
            print('** instance id missing **')
            return
        new_key = class_name + '.' + class_id
        try:
            print(storage._FileStorage__objects[new_key])
        except BaseException:
            print("** no instance found **")

    def do_destroy(self, arg):
        """ delete instance """
        n_args = ""
        class_name = ""
        class_id = ""
        try:
            n_args = arg.split(" ")
            class_name = n_args[0]
            class_id = n_args[1]
        except BaseException:
            pass
        if not class_name:
            print('** class name missing **')
        elif class_name not in Class_Dict:
            print("** class doesn't exist **")
        elif not class_id:
            print("** instance id missing **")
        else:
            new_key = class_name + '.' + class_id
            try:
                del(storage._FileStorage__objects[new_key])
                storage.save()
            except KeyError:
                print("** no instance found **")

    def help_destroy(self):
        """ destroy help """
        print('Destroy command to show delete an instance based\
            on class name and id\n')

    def do_all(self, arg):
        """ print all """
        n_list = []
        if arg:
            if arg not in Class_Dict:
                print("** class doesn't exist **")
                return
            for key, value in storage._FileStorage__objects.items():
                if key.split(".")[0] == arg:
                    n_list.append(str(value))
        else:
            for key, value in storage._FileStorage__objects.items():
                n_list.append(str(value))
        print(n_list)

    def help_all(self):
        """ help all """
        print("displays all instances [based on class if chosen]")
        print("all [class]")

    def do_update(self, args):
        """ update """
        n_object = ""
        c_name = ""
        c_id = ""
        at_name = ""
        at_val = ""
        objs = ""
        try:
            n_object = args.split(" ")
            c_name = n_object[0]
            c_id = n_object[1]
            at_name = n_object[2]
            at_val = n_object[3]
            objs = storage._FileStorage__objects.items()
        except (IndexError, NameError):
            pass
        if not c_name:
            print("** class name missing **")
            return
        if c_name not in Class_Dict:
            print("** class doesn't exist **")
            return
        if not c_id:
            print("** instance id missing **")
            return
        if not at_name:
            print("** attribute name missing **")
            return
        if not at_val:
            print("** value missing **")
            return
        new_key = c_name + "." + c_id
        store = ["id", "created_at", "updated_at"]
        for key, value in storage._FileStorage__objects.items():
            if new_key not in store:
                if new_key == key:
                    setattr(value, at_name, at_val)
                    new = value
                    new.save()
        if new_key not in storage._FileStorage__objects.keys():
            print("** no instance found **")

    def help_update(self):
        """ update help """
        print("updates and objects with new information")
        print("update <class> <id> <attribute> <value>")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
