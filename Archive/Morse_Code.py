# Write a program that asks the user to enter a string. Then, convert this string to Morse code.

def main(): # Create the main function
	string = input("Please enter a string that you wish to convert to morse code: ")
	raw = [] # Generate a raw list to hold the contents of the string
	raw_cleaned = [] # Generate a new list to hold the cleaned values
	morse_code_output = [] # Generate a new list to hold the morse code output

	for words in string: # For all the words that are in the string
		for characters in words: # For each of the characters in each word
			raw.append(characters) # Append the raw list with each of the characters from the string

	# Create a dictionary with the key value pairs representing possible morse code values
	morse = { ' ' : ' ', ',':'--..--', ".":'.-.-.-', "?":'..--..', '0': '-----', '1': '.----',
	'2': '..---', '3': '...--', '4': '....-', '5': '.....', '6': '-....', '7': '--...', '8': '---..',
	'9': '----.', 'a': '.-', 'b': '-...', 'c': '-.-.', 'd': '-..', 'e': '.', 'f': '..-.', 'g': '--.',
	'h': '....', 'i': '..',	'j': '.---', 'k': '-.-.', 'l': '.-..', 'm': '--', 'n': '-.', 'o': '---',
	'p': '.--.', 'q': '--.-', 'r': '.-.', 's': '...', 't': '-', 'u': '..-', 'v': '...-', 'w': '.--',
	'x': '-..-', 'y': '-.-', 'z': '--..' }

	for a in raw: # For each of the elemnets in a
		if a.isupper(): # If each element in a is an upper value
			raw_cleaned.append(a.lower()) # Add the letter to the new list (need to do this with replace)
		else:
			raw_cleaned.append(a) # Skip over the letter and append the character as is

	for b in raw_cleaned: # For each of the characters in the raw cleaned list
		if b in morse: # If the character is in the dictionary
			morse_code_output.append(morse[b]) # Add the character to the output list
		else:
			morse_code_output.append("Error") # Add the term error to the output list

	print("You entered the following string:", string)
	print("This converts to the following output:")
	print(''.join(morse_code_output)) # Note that .join converts the list items to a string
	#print(morse_code_output) # Print list containing the morse code string rather than the string
		
main() # Call the main function
