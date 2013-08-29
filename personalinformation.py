# Create a personal information class which holds the following information about a user
# Name, address, age, and phone number. Write appropriate accessor and mutator methods
# Also, write a program that creates three instances of that class.
# One instance should hold your information, and the other two should hold your 
# friends' or family members' information

class PersonalInfo: # Create the personal information class
	"""docstring for PersonalInfo"""
	def __init__(self, name, address, age, phone):
		self.__name = name
		self.__address = address
		self.__age = age
		self.__phone = phone

	def set_name(self, name): # Mutator method
		self.__name = name

	def set_address(self, address): # Mutator method
		self.__address = address

	def set_age(self, age): # Mutator method
		self.__age = age

	def set_phone(self, phone): # Mutator method
		self.__phone = phone

	def get_name(self): # Accessor method
		return self.__name

	def get_address(self): # Accessor method
		return self.__address

	def get_age(self): # Accessor method
		return self.__age

	def get_phone(self): # Accessor method
		return self.__phone
		