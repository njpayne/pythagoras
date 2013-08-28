# Write a program that prompts the user to enter a number within a range of
# 1 through 10. The program should display the relevant roman numeral for
# that number. Here is the list of roman numerals.
# 1 - I, 2 - II, 2 - III, 4 - IV, 5 - V, 6 - VI, 7 - VII, 8 - VIII, 9 - IX, 10 - X

print("This program converts standard numbers to roman numbers!")
num = int(input("Please enter a number between the range of 1 and 10: "))

def conversion(x): # Could also write this using a case
	if x == 1: # This converts the value of 1
		print("You entered the number", num)
		print("This converts to the roman numeral I")
	elif x == 2: # This converts the value of 2
		print("You entered the number", num)
		print("This converts to the roman numeral II")
	elif x == 3: # This converts the value of 3
		print("You entered the number", num)
		print("This converts to the roman numeral III")
	elif x == 4: # This converts the value of 4
		print("You entered the number", num)
		print("This converts to the roman numeral IV")
	elif x == 5: # this converts the value of 5
		print("You entered the number", num)
		print("This converts to the roman numeral V")
	elif x == 6: # This converts the value of 6
		print("You entered the number", num)
		print("This converts to the roman numeral VI")
	elif x == 7: # This converts the value of 7
		print("You entered the number", num)
		print("This converts to the roman numeral VII")
	elif x == 8: # This converts the value of 8
		print("You entered the number", num)
		print("This converts to the roman numeral VIII")
	elif x == 9: # This converts the value of 9
		print("You entered the number", num)
		print("This converts to the roman numeral IX")
	elif x == 10: # This converts the value of 10
		print("You entered the number", num)
		print("This converts to the roman numeral X")
	else: # This deals with the undefined case
		print("You did not enter a number between 1 and 10.")
		print("Please work on your reading!")

print("") # Print a space 
conversion(num) # Call the conversion function
