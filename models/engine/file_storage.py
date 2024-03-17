#!/usr/bin/python3
"""
FileStorage Module

	Author: Arafa Khalaf <khalafarafa@gmail.com>
	Version: 1.0
"""

import json
from os import path

class FileStorage:
    """
    A class for
        serializing instances to a JSON file
        deserializing JSON files to instances.

    Private class attributes:
        __file_path: string - path to the JSON file (ex: file.json)
        __objects: dictionary - empty
            but will store all objects by <class name>.id
                    (ex: to store a BaseModel object with id=12121212,
                    the key will be BaseModel.12121212)

    Public instance methods:
        all(self):
        	returns the dictionary __objects
        new(self, obj):
        	sets in __objects the obj with key <obj class name>.id
        save(self):
        	serializes __objects to the JSON file (path: __file_path)
        reload(self):
        	deserializes the JSON file to __objects
            (only if the JSON file (__file_path) exists; otherwise, do nothing.
            If the file doesn’t exist, no exception should be raised)
    """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        Method:
            Get de dictionary __objects.
        Return:
        	the dictionary __objects."""
        return self.__objects

    def new(self, obj):
        """
        Method:
        	Sets in __objects the obj with key <obj class name>.id.

        Args:
            obj: An instance of a class to be stored in __objects.
        """
        key = "{}.{}".format(type(obj).__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """
        Method:
        	Serializes __objects to the JSON file.(path: __file_path)
        """
        serialized_objects = {}
        for key, obj in self.__objects.items():
            serialized_objects[key] = obj.to_dict()
        with open(self.__file_path, 'w') as file:
            json.dump(serialized_objects, file)

    def reload(self):
        """
        Method:
        	Deserializes the JSON file to __objects."""
        if path.exists(self.__file_path):
            with open(self.__file_path, 'r') as file:
                try:
                    serialized_objects = json.load(file)
                    for key, obj_dict in serialized_objects.items():
                        class_name, obj_id = key.split('.')
                        module = __import__('models.' + class_name, fromlist=[class_name])
                        class_ = getattr(module, class_name)
                        obj = class_(**obj_dict)
                        self.__objects[key] = obj
                except json.JSONDecodeError:
                    pass  # File is empty or invalid JSON
