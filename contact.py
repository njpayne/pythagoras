# Create a contact class to be used as the basis for a new address book

class Contact: # Create the new contact class
	"""docstring for Contact"""
	def __init__(self, name, phone, email): # Define the initializer function
		self.__name = name
		self.__phone = phone
		self.__email = email

	def set_name(self, name): # Set the name attributes
		self.__name = name

	def set_phone(self, phone): # Set the phone attributes
		self.__phone = phone

	def set_email(self, email): # Set the email attributes
		self.__email = email

	def get_name(self):
		return self.__name

	def get_phone(self):
		return self.__phone

	def get_email(self):
		return self.__email

	# Return the object's state as a string using __str__
	def __str__(self):
		return "Name: " + self.__name + "\nPhone: " + self.__phone + "\nEmail: " + self.__email

