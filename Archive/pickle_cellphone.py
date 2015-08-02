# The pickle module provides functions for serializing objects
# Serializing an object means converting it into a stream of bytes that can be saved to a file for later retrieval
# The pickle modules dump function serializes an object and writes it to a file
# The load function retrieves an object from a file and deserializes it (unpickles it)

import pickle
import cellphone

FILENAME = 'cellphones.dat' # This is the constant representing the file name

def main(): # Create the main function
	again = 'y' # Initialize a variable to control the loop
	output_file = open(FILENAME, 'wb') # Write back to the file that is open & which was created above

	while again.lower() == 'y': # While the again = 'y'
		man = input("Please enter the manufacturer: ")
		mod = input("Please enter the model: ")
		retail = float(input("Please enter the retail price: "))

		phone = cellphone.CellPhone(man, mod, retail) # Create the cell phone object
		pickle.dump(phone, output_file) # Pickle the object and send it to the output_file
		again = input("Would you like to enter more phone data? (y/n): ")

	output_file.close() # Close the file in question
	print("The data was written to", FILENAME)

main() # Call the main function