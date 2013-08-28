# Program demonstrating object oriented programming in Python through the coin flip

import random # Import the random module

# Create a coin class. This class is code that specifies the data attributes and methods for a particular object
# Note that the __init__ method initializes the sideup data attribute

class Coin: # Create the coin class. This is the cookie cutter that the objects will be built on
	"""docstring for Coin"""
	def __init__(self):
		#self.sideup = 'Heads' # This statement assigns heads to the side-up data attribute belonging to the object that was just created
		self.__sideup = 'Heads' # Note that this approach allows me to hide the attribute; Thus, outside code cannot access it
		
		# Note that __init__ creates the first method. This method is automatically executed and is usually the first method inside a class definition
		# when an instance of the class is created in memory (hence its name as an initializer method)
		# Note also that the self parameter is required in every method  of a class. You don't have to name it self. That said,
		# the naming of this parameter is strongly recommended in order to make sure that this conforms with standard practice

	def toss(self): # Create a toss method that generates a random number in the range of 0 through 1
		if random.randint(0,1) == 0:
			self.__sideup = 'Heads' # If the random number generated is a 0, then return heads
		else:
			self.__sideup = 'Tails' # Otherwise, return tails if the number is 1

	def get_sideup(self): # This method returns the value of the self parameter
		return self.__sideup # This parameter can be used in the main program

def main(): # Create the main function
	my_Coin = Coin() # Create a new object from the Coin class above
	tails = 0 # Create a counter to keep track of the number of tails
	heads = 0 # Create a counter to keep track of the number of heads
	
	times = int(input("How many times would you like to toss the coin? "))
	print("Below is your list of results from the coin flip:")
	
	for x in range(0,times):
		my_Coin.toss() # Toss the coin to generate the heads or tails call
		print(my_Coin.get_sideup()) # This can be optional

		if my_Coin.get_sideup() == 'Heads': # If the coin flip results in a head, then add 1 to the head counter
			heads += 1 # Add 1 to the head counter
		else:
			tails += 1 # Otherwise, add 1 to the tail counter

	print("After running your program, your coin flipped a total of", heads, "heads and ", tails, "tails!")

main() # Call the main function


