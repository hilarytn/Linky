#!/usr/bin/python3
import cmd
import time
from models.base_model import BaseModel
#from models.base_model import classes
from models.user import User
from models.vendor import Vendor
from models import storage
from models.engine.file_storage import FileStorage
import re


class Linky(cmd.Cmd):
    prompt = "Linky>>> "

    def default(self, line):
        pass
        

    def do_quit(self, arg):
        """Quit the console by typing 'quit' and pressing the 'Enter' button"""
        print("Quitting...")
        time.sleep(0.6)
        print("Bye")
        return True

    def do_EOF(self, line):
        """EOF signifies the end of file. Can serve as Termination point for the console."""
        return True

    def do_create(self, line):
        """Creates an object. Used as `create <class name>` """
        data = line.split()
        if len(data) == 0:
            print("** class name missing **")

        if len(data) > 0 and data[0] not in storage.classes():
            print("** class doesn't exist **")

        if len(data) >= 1 and data[0] and data[0] == 'Vendor':
            if len(data) < 5:
                print("** use format: `create Vendor <first name> <surname> <email> <address>` **")
                return 
            else:
                instance = globals()[data[0]](data[1], data[2], data[3], data[4])
                instance.save()
                print(instance.id)
                return

        if len(data) >= 1 and data[0] and data[0] == 'User':
            if len(data) < 5:
                print("** use format: `create User <first name> <surname> <email> <password>` **")
                return
            else:
                instance = globals()[data[0]](data[1], data[2], data[3], data[4])
                instance.save()
                print(instance.id)
                return 

        if len(data) >= 1 and data[0] in storage.classes():
            instance = globals()[data[0]]()
            instance.save()
            print(instance.id)


    def do_show(self, line):
        data = line.split()
        if len(data) == 0:
            print("** class name missing **")
        if len(data) > 0 and data[0] not in storage.classes():
            print("** class doesn't exist **")
        if len(data) == 1 and data[0] in storage.classes():
            print("** instance id missing **")
        if len(data) == 2 and data[0] in storage.classes() and data[1]:
            key = "{}.{}".format(data[0], data[1])
            if key in storage.all():
                print( storage.all()[key])
            else:
                print("** no instance found **")

    def do_all(self, line):
        data = line.split()
        if len(data) == 0:
            print("** class name missing **")

        if len(data) > 0 and data[0] not in storage.classes():
            print("** class doesn't exist **")

        if len(data) == 1 and data[0] in storage.classes():
            for k, v in storage.all().items():
                if v.__class__.__name__ == data[0]:
                    print(v)

    def do_destroy(self, line):
        data = line.split()
        if len(data) == 0:
            print("** class name missing **")
        elif len(data) > 0 and data[0] not in storage.classes():
            print("** class doesn't exist **")
        elif len(data) == 1 and data[0] in storage.classes():
            print("** instance id missing **")
        elif len(data) == 2 and data[0] in storage.classes() and data[1]:
            for k, v in storage.all().items():
                if v.id == data[1]:
                    del storage.all()[k]
                    storage.save()
                    return
            print("** no instance found **")

    def do_update(self, line):
        data = line.split()


if __name__ == "__main__":
    my_intro = """
    *****************************************************
    *     Hello, Welcome to the Linky Console Session.  *
    *     You can begin by typing 'help <option>' for   *
    *     details about a particular command. Or type   *
    *     just 'help' for a general overview.           * 
    *                                                   *
    *       Authors:  - Hilary Titus Naor               *
    *                 - Christopher Nnamdi              *
    *****************************************************
    """
    Linky().cmdloop(intro=my_intro)
