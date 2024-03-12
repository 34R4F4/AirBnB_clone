#!/usr/bin/python3
"""
Content:
    * Create a unique FileStorage instance for your application.

Description:
    Module:
    initializes unique instance of the FileStorage class for the application.

    The FileStorage instance is used for
        serializing instances to a JSON file and deserializing

    JSON files to instances.
        It provides a mechanism for persistent storage
        and retrieval of objects in the application.

Usage:
    The `storage` variable is created as an instance of the FileStorage class.
    It is initialized with data
        from the JSON file specified in the `FileStorage` class.
    The `reload()` method
        is called to load data from the JSON file into memory.
    This allows existing objects to be restored
    from the JSON file when the application starts.

Example:
    from models.engine.file_storage import FileStorage

    # Create a unique FileStorage instance for the application
    storage = FileStorage()
    storage.reload()
"""

from models.engine.file_storage import FileStorage

# Create a unique FileStorage instance for the application
storage = FileStorage()
storage.reload()
