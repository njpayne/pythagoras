# One foot equals 12 inches. Write a program with a function that accepts a number of feet
# as an input and returns the number of inches in those fet. Use the function
# in a program that prompts the user to enter a number and then displays the number of feet

def main():
	print("The following is a foot to inches converter!")
	feet = float(input("Please enter the total number of feet that you wish to convert: "))
	print("") # Print a blank line!
	print("You asked me to convert", 
		format(feet, ".2f"), "feet to inches!")
	print(format(feet, ".2f"), 
		"feet, is equal to a total of", 
		format(conversion(feet), ".2f"), 
		"inches!")
	print("Thank you for using this calcualtor!")

def conversion(x): # Create the conversion function
	inches = x * 12 # Convert feet to inches
	return inches # return inches

main() # Call the main function
