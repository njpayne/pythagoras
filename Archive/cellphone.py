# Create a class that represents cellphone data. Then, add a manufacturer, model, and retail price to the class

class CellPhone: # Create the cell phone class
	"""docstring for CellPhone""" # This is the cell phone class that will be the framework for the individual objects
	def __init__(self, manufac, model, retailprice): # The init class is automatically executed every time the 
		self.__manufac = manufac # Accept the initial argument for the manufacturing data
		self.__model = model # Accept the initial argument for the model data
		self.__retailprice = retailprice # Accept the initial argument for the price data
		# Remember that __price enables us to hide the attribute (make it private)

	# Need first to create separate methods for each of the object parameters
	# The methods below accept arguments for each of the parameters
	def set_manufact(self, manufac): # Accept the argument for the manufacturer
		self.__manufac = manufac # This is a mutator method

	def set_model(self, model): # Accept the argument for the model
		self.__model = model # This is a mutator method

	def set_retailprice(self, retailprice): # Accept the argument for the price
		self.__retailprice = retailprice # This is a mutator method

	# The following methods operate when the user asks for value of the object to be return
	def get_manufac(self): # This is an accessor method
		return self.__manufac 

	def get_model(self): # This is an accessor method
		return self.__model

	def get_retailprice(self): # This is an accessor method
		return self.__retailprice

def main(): # Create a basic function to test the cellphone class
	# Let us get all the phone data
	man = input("Please input the name of the manufacturer for this cellphone: ")
	model = input("Please input the name of the model for this cellphone: ")
	price = float(input("Please input the price of this cellphone: "))

	# Create an instance of the CellPhone class
	phone = CellPhone(man, model, price) # This class is created using the three inputs which are passed to the new object

	# Display the data that was entered
	print("The manufacturer of your phone is:", phone.get_manufac()) # Note that phone is the object and get_manufac() is the method
	print("The model of your phone is:", phone.get_model()) # Note that phone is the object and get_model() is the method acting on it
	print("The price of your phone is:", phone.get_retailprice()) # Note that phone is the object and get_model() is the method acting on it

main() # Call the main function
