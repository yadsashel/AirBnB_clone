#!/usr/bin/python3
"""Defines the HBnB console."""
import cmd
import re
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


def parse(arg):
    """Parse input arguments."""
    # Regex to match curly braces or brackets
    curly_braces = re.search(r"\{(.*?)\}", arg)
    brackets = re.search(r"\[(.*?)\]", arg)

    # Determine argument parsing based on curly braces or brackets
    if curly_braces is None:
        if brackets is None:
            return [i.strip(",") for i in arg.split()]
        else:
            lexer = arg[:brackets.span()[0]].split()
            retl = [i.strip(",") for i in lexer]
            retl.append(brackets.group())
            return retl
    else:
        lexer = arg[:curly_braces.span()[0]].split()
        retl = [i.strip(",") for i in lexer]
        retl.append(curly_braces.group())
        return retl


class HBNBCommand(cmd.Cmd):
    """Defines the HolbertonBnB command interpreter."""

    prompt = "(hbnb) "
    __classes = {
        "BaseModel",
        "User",
        "State",
        "City",
        "Place",
        "Amenity",
        "Review"
    }

    def emptyline(self):
        """Do nothing upon receiving an empty line."""
        pass

    def default(self, arg):
        """Default behavior for cmd module when input is invalid."""
        argdict = {
            "all": self.do_all,
            "show": self.do_show,
            "destroy": self.do_destroy,
            "count": self.do_count,
            "update": self.do_update
        }
        match = re.search(r"\.", arg)
        if match is not None:
            argl = arg.split(".", 1)
            command = argl[1].split("(", 1)
            if command[0] in argdict.keys():
                call = "{} {}".format(argl[0], command[1][:-1])
                return argdict[command[0]](call)
        print("*** Unknown syntax: {}".format(arg))
        return False

    def do_quit(self, arg):
        """Quit command to exit the program."""
        return True

    def do_EOF(self, arg):
        """EOF signal to exit the program."""
        print("")
        return True

    def do_create(self, arg):
        """Create a new class instance."""
        argl = parse(arg)
        if not argl:
            print("** class name missing **")
            return False
        if argl[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
            return False
        new_instance = eval(argl[0])()
        new_instance.save()
        print(new_instance.id)

    def do_show(self, arg):
        """Display the string representation of a class instance."""
        argl = parse(arg)
        if len(argl) == 0:
            print("** class name missing **")
            return False
        if argl[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
            return False
        if len(argl) == 1:
            print("** instance id missing **")
            return False
        key = "{}.{}".format(argl[0], argl[1])
        objdict = storage.all()
        if key not in objdict:
            print("** no instance found **")
            return False
        print(objdict[key])

    def do_destroy(self, arg):
        """Delete a class instance."""
        argl = parse(arg)
        if len(argl) == 0:
            print("** class name missing **")
            return False
        if argl[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
            return False
        if len(argl) == 1:
            print("** instance id missing **")
            return False
        key = "{}.{}".format(argl[0], argl[1])
        objdict = storage.all()
        if key not in objdict:
            print("** no instance found **")
            return False
        del objdict[key]
        storage.save()

    def do_all(self, arg):
        """Display string representations of all instances."""
        argl = parse(arg)
        objlist = []
        if argl and argl[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
            return False
        for obj in storage.all().values():
            if not argl or obj.__class__.__name__ == argl[0]:
                objlist.append(str(obj))
        print(objlist)

    def do_count(self, arg):
        """Retrieve the number of instances of a given class."""
        argl = parse(arg)
        count = 0
        if not argl:
            print("** class name missing **")
            return False
        if argl[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
            return False
        for obj in storage.all().values():
            if obj.__class__.__name__ == argl[0]:
                count += 1
        print(count)

    def do_update(self, arg):
        """Update a class instance."""
        argl = parse(arg)
        if len(argl) < 3:
            print("** class name missing **")
            return False
        if argl[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
            return False
        if len(argl) < 4:
            print("** instance id missing **")
            return False
        key = "{}.{}".format(argl[0], argl[1])
        objdict = storage.all()
        if key not in objdict:
            print("** no instance found **")
            return False
        obj = objdict[key]
        if len(argl) < 5:
            print("** attribute name missing **")
            return False
        if len(argl) < 6:
            print("** value missing **")
            return False
        setattr(obj, argl[3], eval(argl[4]))
        storage.save()


if __name__ == "__main__":
    HBNBCommand().cmdloop()
