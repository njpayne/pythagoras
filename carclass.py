# Create a car class which holds the following information about cars
# Year, make, model; then, create methods which do the following:
# a) Accelerate, which adds 5 to the speed data every time it is callled
# b) Brake, which should take away 5 from the speed data every time it is callled
# c) Get_Speed, which should return the current speed of the car and display it

class Car: # Create the initial car class
	"""docstring for Car""" # Docstring for the car class
	def __init__(self, year, make, model):
		self.__year = year # Holds the year attributes
		self.__make = make # Holds the make attributes
		self.__model = model # Holds the model attributes

	def set_year(self, year): # Set the year attributes; Mutator method
		self.__year = year # Holds the year attributes

	def set_make(self, make): # Set the make attributes; Mutator method
		self.__make = make # Holds the make attributes

	def set_model(self, model): # Set the model attributes; Mutator method
		self.__model = model # Holds the model attributes

	def get_year(self): # Accessor method
		return self.__year

	def get_make(self): # Accessor method
		return self.__make

	def get_model(self): # Accessor method
		return self.__model
