# Create a class named Pet which holds the following data attributes about each Pet
# Name, Animal Type, Age ; Once completed, developed a test program to accept values for these attributes

class Pet: # Create the pet class to hold the attributes about each pet
	"""docstring for Pet"""
	def __init__(self, name, animaltype, age):
		self.__name = name # Hold the attribute age
		self.__animaltype = animaltype # Hold the attribute animal type
		self.__age = age # Hold the attributed age

	def set_name(self, name): # Mutator method
		self.__name = name

	def set_animaltype(self, animaltype): # Mutator method
		self.__animaltype = animaltype 

	def set_age(self, age): # Mutator method
		self.__age = age # Hold the attributed age

	def get_name(self): # Accessor method
		return self.__name

	def get_animaltype(self): # Accessor method
		return self.__animaltype

	def get_age(self): # Accessor method
		return self.__age

# print(Pet) # Print out the Pet class information
