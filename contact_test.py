import contact

def main(): # Create a basic function to test the cellphone class
	# Let us get all the phone data
	a = input("Please input the name of your contact: ")
	b = input("Please input the phone number of your contact: ")
	c = input("Please input the e-mail of your contact: ")

	# Create an instance of the CellPhone class
	address = contact.Contact(a, b, c) # This class is created using the three inputs which are passed to the new object

	# Display the data that was entered
	print("The name of your contact is:", address.get_name()) 
	print("The phone number of your contact is:", address.get_phone()) 
	print("The email of your contact is:", address.get_email()) 

main() # Call the main function