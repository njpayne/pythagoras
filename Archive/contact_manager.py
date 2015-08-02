# Create a base program that manages contacts created using the Contact class
# This specific program will keep the contacts objects in a dictionary
# Each time a new object is added, the contact object holding the specific data would be
# Stored as a value in the dictionary; Note that the name would be the primary key
# The other attributes would be the values
# The program below will also automatically pickle the dictionary and save it to a file
# every time the user quits the program

import contact # Import the initial contact file
import pickle # Used to serialize the file later as needed

# Define all relevant menu choices
LOOK_UP = 1
ADD = 2
CHANGE = 3
DELETE = 4
QUIT = 5

FILENAME = 'contacts.dat' # Create the global file for use with the contacts dB;
# The dictionary will be pickled to this location (the objects serialized), on exit

def main(): # Create the main function
	mycontacts = load_contacts() # Load the existing contact dictionary and assign it to mycontacts
	choice = 0 # Initialize a variable for the user's choice

	# Process the new selectinos until the user wants to quit the program
	while choice != QUIT:
		choice = get_menu_choice()

		# Process the choices
		if choice == LOOK_UP: # Look-up
			look_up(mycontacts)
		elif choice == ADD: # Add
			add(mycontacts)
		elif choice == CHANGE: # Change
			change(mycontacts)
		elif choice == DELETE: # Delete
			delete(mycontacts)

	# Save the new contacts dictionary to the data file
	save_contacts(mycontacts)

# Create all relevant functions for the program
def load_contacts(): # Try to load the contacts in from the data file and unpickle them
	try:
		input_file = open(FILENAME, 'rb') # Read binary
		contact_dct = pickle.load(input_file) # Define the contact_dictionary
		input_file.close() # Close the contact file
	except IOError: # If there is an error when bringing in the file
		contact_dct = {} # Create an empty dictionary since the file could not be opened

	return	contact_dct # Return the contact dictionary

def get_menu_choice():
	print("")
	print("Menu")
	print("----------------------")
	print("1. Look up a contact")
	print("2. Add a new contact")
	print("3. Change an existing contact")
	print("4. Delete a contact")
	print("5. Quit the program")
	print("")

	# Ask the user to make a choice
	choice = int(input("Please enter the choice that you would like to make: "))

	# Validate the choice that is being made
	while choice < LOOK_UP or choice > QUIT:
		choice = int(input("The choice you entered was incorrect. Please make a correct choice!"))

	return choice # Return the users choice

def look_up(mycontacts):
	name = input("Please enter a name to look for in the system: ")
	# Look up the name in my dictionary
	print(mycontacts.get(name, "That name is not found"))
	# This function looks up the specified contact using the get dictionary functionality
	# If the name is found as a key in the dictionary, the get method returns the reference ot that object
	# If it is not found, the get method returns the string message letting the user know

def add(mycontacts): # Add a new entry into the specified dictionary
	name = input("Name: ") # Get the name
	phone = input("Phone: ") # Get the phone
	email = input("Email: ") # Get the email

	entry = contact.Contact(name, phone, email) # Create a new object using the Contact class

	# If the name does not exist, add it as a key
	if name not in mycontacts:
		mycontacts[name] = entry
		print("The entry has been added!")
	else:
		print("That name already exists in the management system!")

def change(mycontacts): # Change a current entry in the database
	name = input("Please input a name to lookup: ")

	if name in mycontacts: # If the name is in the mycontacts database
		phone = input("Enter a new phone number: ")
		email = input("Enter a new email address: ")

		entry = contact.Contact(name, phone, email) # Create a new contact entry
		mycontacts[name] = entry # Update the entry in the current dictionary with the new object
		print("Information updated!")
	else:
		print("That name is not found")

def delete(mycontacts): # Delete an entry from the database
	name = input("Please enter a name to look-up in the database: ")
	if name in mycontacts:
		del mycontacts[name] # Delete the entry from the dictionary
		print("Entry deleted!")
	else:
		print("That name is not found!")

def save_contacts(mycontacts): # Pickle the current mycontacts dictionary and save it
	output_file = open(FILENAME, 'wb') # Write binary
	pickle.dump(mycontacts, output_file) # Dump the file into the folder in question
	output_file.close() # Close the file

main() # Call the main function
