# Create a program the unpickles the CellPhone object

import pickle
import cellphone

FILENAME = 'cellphones.dat' # Refer to the name of the file that is currently in question

def main(): # Create the main function
	end_of_file = False # To indicate the end of the file

	input_file = open(FILENAME, 'rb') # Input and open the file in question

	while not end_of_file: # While we are not at the end of the file
		try:
			phone = pickle.load(input_file) #Unpickle the next object
			display_data(phone) # Display the cell phone data (read the value of the object)

		except EOFError:
			end_of_file = True

	input_file.close() # Close the file in question

def display_data(phone): # Create the display_data function
	print("Manufacturer: ", phone.get_manufac())
	print("Model Number: ", phone.get_model())
	print("Retail price: ", 
		format(phone.get_retailprice(), ',.2f'),sep='')
	print('') # Print a blank line

main() # Call the main function