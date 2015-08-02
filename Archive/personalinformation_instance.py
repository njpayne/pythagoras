# Create multiple instances of the the personal information object

import personalinformation

def main(): # Create the main function
	client_list = [] # Create an empty client list that holds objects, which are individual clients
	print("Welcome to the client list generator!")
	print("Please enter the information for 3 clients (the first client being yourself of course!")

	for x in range(1,4): # For the number of users that are specified
		nam = input("Please enter the user's name: ")
		add = input("Please enter the user's address: ")
		ag = input("Please enter the user's age: ")
		ph = input("Please enter the user's phone number: ")

		client = personalinformation.PersonalInfo(nam, add, ag, ph) # Create a new object with each set of supplied information
		client_list.append(client) # Append the client list with the new information

	print("")
	for a in client_list: # For each of the objects within the client list
		print("The name of your client is", a.get_name())
		print("The address of your client is", a.get_address())
		print("The age of your client is", a.get_age())
		print("The phone number of your client is", a.get_phone())
		
main() # Call the main function
