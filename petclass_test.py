# Create a set of commands to test out the Pet Class

import petclass # Import the file titled petclass which holds the Pet class

def main(): # Create the main function
	pet_list = [] # Create an empty list which will be full of pet objects

	print("Welcome to the pet management system!")
	print("The system below helps you manage your current pet inventory!")
	print("Please note that each pet has a name, animal type, and age that you can give it!")
	option = input("Would you like to add an animal to the pet management system? (y or n) ")
	
	counter = 1
	while option.lower() == 'y':
		print("Please enter the information for pet", counter)
		name = input("Please enter the name of your current pet! ")
		animaltype = input("Please enter the type of animal! ")
		age = int(input("Please enter the age of this animal (as an integer): "))

		pet_object = petclass.Pet(name, animaltype, age) # Create a new pet object
		pet_list.append(pet_object) # Append the pet list with the newly created pet object
		option = input("Would you like to add another animal to the pet management system? (y or n) ")
		counter += 1

	print("")
	print("") # Thank you for using the pet information system
	print("You entered the following pets inside the system.")

	counter = 1
	for x in pet_list: # For each of the objects in the pet list
		print("Pet Number:", counter)
		print("Name:", x.get_name())
		print("Animal Type:", x.get_animaltype())
		print("Age:", x.get_age())
		counter += 1

main() # Call the main function
