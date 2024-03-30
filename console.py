#!/usr/bin/python3
"""Command Line Interpreter v2"""
import cmd
import re
import json
from models import storage


class HBNBCommand(cmd.Cmd):
    """Command Line Interpreter for managing objects"""

    prompt = "(hbnb) "

    def default(self, line):
        """Handle non-standard commands."""
        self._precmd(line)

    def _precmd(self, line):
        """Intercept and preprocess commands."""
        match = re.search(r"^(\w*)\.(\w+)(?:\(([^)]*)\))?$", line)
        if not match:
            return line
        class_name, method, args = match.groups()
        if args:
            args = self._parse_args(args)
        return f"{method} {class_name} {args}"

    def _parse_args(self, args_str):
        """Parse arguments and convert them into a string."""
        match = re.search(r'^"([^"]*)"(?:,\s*(.+))?$', args_str)
        if match:
            mg1 = match.group(1)
            mg2 = match.group(2)
            return f"{mg1} {mg2 if mg2 else ''}"
        return args_str

    def do_EOF(self, line):
        """Exit the program gracefully."""
        print()
        return True

    def do_quit(self, line):
        """Exit the program."""
        return True

    def do_create(self, line):
        """Create a new instance."""
        if not line:
            print("** class name missing **")
            return
        class_name = line.split()[0]
        if class_name not in storage.classes():
            print("** class doesn't exist **")
            return
        instance = storage.classes()[class_name]()
        instance.save()
        print(instance.id)

    def do_show(self, line):
        """Show details of a specific instance."""
        class_name, instance_id = self._parse_line(line, 2)
        if not class_name or not instance_id:
            return
        key = f"{class_name}.{instance_id}"
        if key not in storage.all():
            print("** no instance found **")
            return
        print(storage.all()[key])

    def do_destroy(self, line):
        """Delete a specific instance."""
        class_name, instance_id = self._parse_line(line, 2)
        if not class_name or not instance_id:
            return
        key = f"{class_name}.{instance_id}"
        if key not in storage.all():
            print("** no instance found **")
            return
        del storage.all()[key]
        storage.save()

    def do_all(self, line):
        """Show all instances or instances of a specific class."""
        class_name = line.split()[0] if line else None
        if class_name and class_name not in storage.classes():
            print("** class doesn't exist **")
            return
        instances = [str(obj) for key, obj in storage.all().items()
                     if not class_name or key.startswith(class_name+'.')]
        print(instances)

    def do_count(self, line):
        """Count instances of a specified class."""
        class_name = line.strip().split()[0] if line else None
        if not class_name:
            print("** class name missing **")
            return
        if class_name not in storage.classes():
            print("** class doesn't exist **")
            return
        count = sum(1 for key in storage.all() if key.startswith(
            class_name+'.'))
        print(count)

    def do_update(self, line):
        """Update an instance's attributes."""
        class_name, instance_id, attribute, value = self._parse_line(line, 4)
        if not all((class_name, instance_id, attribute, value)):
            return
        key = f"{class_name}.{instance_id}"
        if key not in storage.all():
            print("** no instance found **")
            return
        instance = storage.all()[key]
        setattr(instance, attribute, value)
        instance.save()

    def _parse_line(self, line, expected_parts):
        """Parse command line into parts."""
        parts = line.split(' ')
        if len(parts) < expected_parts:
            print("** missing arguments **")
            return (None,) * expected_parts
        return tuple(parts[:expected_parts])


if __name__ == '__main__':
    HBNBCommand().cmdloop()
