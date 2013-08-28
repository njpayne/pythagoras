# Create a program that takes any telephone number that is input, and returns the base telephone number
# For example, if 555-GET-FOOD is input, return the base telephone number 555-438-3663

def telephone():
	phone = input("Please input the telephone number that you would like to analyze: ")
	phone_number = [] # Create an empty list to hold the original phone number digits
	phone_number_cleaned = [] # Create an empty list to hold the cleaned phone number
	phone_number_final = [] # Create a final list to hold the revised phone number

	# Create the original phone list from the phone input statment
	for x in phone: # For each of the characters in phone
		phone_number.append(x) # Add each of the characters to a list

	# Reduce all upper case letters to lower case and validate / clean data
	for b in phone_number: # For each of the elements in the phone_number list
		if b.isupper(): # Check if the string is upper case
			x = b.lower() # If is is, create a new character that is lower case
			phone_number_cleaned.append(x) # Add new character to the cleaned list
		else:
			phone_number_cleaned.append(b) # Append the cleaned list with the original character

	# Convert the lower case letters to the proper numbers by searching a dictionary
	numbers = {'a': '2', 'b': '2', 'c': '2', 'd': '3', 'e': '3', 'f': '3', 'g': '4', 'h': '4', 'i': '4',
	'j': '5', 'k': '5', 'l': '5', 'm': '6', 'n': '6', 'o': '6', 'p': '7', 'q': '7', 'r': '7', 's': '7', 't': '8',
	'u': '8', 'v': '8', 'w': '8', 'x': '9', 'y': '9', 'z': '9'}

	for a in phone_number_cleaned: # Loop through all the values of the cleaned phone number list
		if a in numbers: # If a matches the key of a key-value pair in the numbers dictionary
			phone_number_final.append(numbers[a])
		else:
			phone_number_final.append(a) # If the value is not within the dictionary, append

	print("You originally entered the following phone number:", phone_number)
	print("This converts to the following numeric phone number:", ''.join(phone_number_final))
	
telephone() # Call the telephone function
