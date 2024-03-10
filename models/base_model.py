#!/usr/bin/python3
"""
BaseModel Module

	Author: Arafa Khalaf
	Version: 1.0
	Path: models/base_model.py
"""

import uuid
from datetime import datetime

class BaseModel:
		"""
		Class:
			BaseModel: defines all common attributes/methods for other classes

		Attributes:
			id (str): The unique identifier for BaseModel.
			created_at (datetime): The creation datetime of the BaseModel.
			updated_at (datetime): The last update datetime of the BaseModel.
		"""

	"""
	Public instance attributes:
		id
		created_at
		updated_at
	"""
	def __init__(self):
		"""
		Initializes the BaseModel Public instance attributes
		(id, created_at, updated_at)
		"""

		"""id"""
		# Creating a unique identifier using uuid.uuid4()
		self.id = uuid.uuid4()
		# Convert the unique identifier to string
		self.id = str(self.id)

		"""created_at"""
		# Set the creation time to the current datetime
		self.created_at = datetime.now()

		"""updated_at"""
		# Set the initial update time to the creation time
		self.updated_at = self.created_at


	"""__str__"""
	def __str__(self):
		"""
		Returns a human-readable representation of of the BaseModel object.

		Returns:
			str: [<class name>] (<self.id>) <self.__dict__>
		"""
		return "[{}] ({}) {}".format(
		self.__class__.__name__, self.id, self.__dict__)


	"""
	Public instance methods:
		save(self)
		to_dict(self)
	"""

	def save(self):
		"""
		updates the public instance attribute updated_at with the current datetime
		"""
		self.updated_at = datetime.now()


	def to_dict(self):
		"""
		Converts the BaseModel instance to a dictionary representation.

		Returns:
			dict: A dictionary containing all keys/values of __dict__ of the instance,
				  along with class name, created_at, and updated_at in ISO format.
		"""
		# Create a dictionary representation of the instance's attributes
		model_dict = self.__dict__.copy()

		# Add '__class__' key with the class name of the object
		model_dict['__class__'] = self.__class__.__name__

		# Convert created_at and updated_at to ISO format strings
		model_dict['created_at'] = self.created_at.isoformat()
		model_dict['updated_at'] = self.updated_at.isoformat()

		return model_dict
