#!/usr/bin/python3
"""Command Line Interpreter"""

import cmd
import json
import re
import sys

from models import storage


class HBNBCommand(cmd.Cmd):
    """Command Line Interpreter for managing objects"""

    prompt = "(hbnb) "

    def do_EOF(self, line):
        """Handle EOF signal"""
        print()
        return True

    def do_quit(self, line):
        """Quit command to exit the program"""
        return True

    def do_create(self, line):
        """Create a new instance of a class"""
        args = line.split()
        if not args:
            print("** class name missing **")
            return

        class_name = args[0]
        if class_name not in storage.classes():
            print("** class doesn't exist **")
            return

        instance = storage.classes()[class_name]()
        instance.save()
        print(instance.id)

    def do_show(self, line):
        """Show details of a specific instance"""
        args = line.split()
        if len(args) < 2:
            print("** class name missing **" if len(args) < 1 else "** instance id missing **")
            return

        class_name, instance_id = args
        if class_name not in storage.classes():
            print("** class doesn't exist **")
            return

        key = f"{class_name}.{instance_id}"
        if key not in storage.all():
            print("** no instance found **")
            return

        print(storage.all()[key])

    def do_destroy(self, line):
        """Delete a specific instance"""
        args = line.split()
        if len(args) < 2:
            print("** class name missing **" if len(args) < 1 else "** instance id missing **")
            return

        class_name, instance_id = args
        if class_name not in storage.classes():
            print("** class doesn't exist **")
            return

        key = f"{class_name}.{instance_id}"
        if key not in storage.all():
            print("** no instance found **")
            return

        del storage.all()[key]
        storage.save()

    def do_all(self, line):
        """Show all instances or instances of a specific class"""
        if not line:
            print([str(obj) for obj in storage.all().values()])
            return

        class_name = line.split()[0]
        if class_name not in storage.classes():
            print("** class doesn't exist **")
            return

        print([str(obj) for key, obj in storage.all().items() if key.startswith(class_name)])

    def do_update(self, line):
        """Update an instance's attributes"""
        args = re.split(r'[,"]+', line)
        if len(args) < 4:
            print("** usage: update <class name> <id> <attribute name> <attribute value> **")
            return

        class_name, instance_id, attribute, value = args[:4]
        if class_name not in storage.classes():
            print("** class doesn't exist **")
            return

        key = f"{class_name}.{instance_id}"
        if key not in storage.all():
            print("** no instance found **")
            return

        instance = storage.all()[key]
        setattr(instance, attribute, value)
        instance.save()

    def do_count(self, line):
        """Count instances of a specified class"""
        class_name = line.strip()
        if class_name not in storage.classes():
            print("** class doesn't exist **")
            return

        count = sum(1 for key in storage.all() if key.startswith(class_name))
        print(count)

    def emptyline(self):
        """Handle empty lines"""
        pass

    def precmd(self, line):
        """Pre-command function"""
        if not sys.stdin.isatty():
            print()

        match = re.match(r'^(\w+)\.(\w+)\(([\s\S]*)\)$', line)
        if match:
            line = f"{match.group(2)} {match.group(1)} {match.group(3)}"
        return line

if __name__ == '__main__':
    HBNBCommand().cmdloop()
