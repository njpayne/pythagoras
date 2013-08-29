# It is common practice to make all of a class's data attributes private and to provide methods for accessing and changing those attributes
# A method that returns a value from a class's attribute but does not change it is known as an accessor method
# Note that get_manufact, get_model, and get_retail_price are alll accessor methods
# On the other hand, a method that stores a value in a data attribute or changes the value of a data attribute
# in some other way is known as a mutator method. These methods control the way that a class's data attributes are modified.
# set_manufac, set_model, and set_retail are mutator methods
# Note that mutator methods are sometimes called "setters" and accessor methods are sometimes called "getters"

# Create a program that creates five CellPhone objects and stores them in a list
import cellphone # Import the cellphone file which contains the cellphone class

def main(): # Create the main function
	phones = make_list() # This is a function which will be outlined below & which will make the list
	print("Here is the data that you entered:")
	display_list(phones)  # This function displays the data in the list

def make_list(): # Define the make list function
	phone_list = [] # Create an empty list

	# Add five cell phones to the list
	for x in range(1,6):
		print("Phone number" + " " + str(x) + ' :') # Print out the number that the user is currently on
		man = input("Please enter the manufacturer: ") # Input the manufacturer
		mod = input("Please enter the model of the phone: ") # Input the model of the phone
		retail = float(input("Please enter the price of the phone: ")) # Input the price of the phone
		print("") # Print a blank line

		# Create a new CellPhone object and assign it in memory
		phone = cellphone.CellPhone(man, mod, retail) # Create the new object
		phone_list.append(phone) # Append the phone_list with the new value

	return phone_list # Return the cell phone list from the function

def display_list(phone_list): # This function acceps the list of CellPhone objects as an argument
	for item in phone_list: # For each item in the list, which is an object
		print(item.get_manufac()) # Print the manufacturer
		print(item.get_model()) # Print the model
		print(item.get_retailprice()) # Print the retail price
		print("")

main() # Call the main function
