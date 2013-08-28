# Write a program that asks a user to enter in a starting element (interger) and then a finishing element (integer)
# The elements correspond to the degrees in celcius. Then, display a table converting the
# degrees in celcius to degrees in farenheigh. The conversion is F = 9/5C + 32
# Use a loop to display the items within a table

def conversion():
	start = int(input("Please enter the starting temperature (Celcius): "))
	finish = int(input("Please enter the ending temperature (Celcius): "))

	print("") # Print a blank space
	print("Celcius\tFarenheight") # Print the table header
	print("------------------------") # Print the divider sign

	for x in range(start, finish + 1, 1): # Start the for loop
		farenheight = 9 / 5 * x + 32 # Formula for converting celcius to farenheight
		print(x, "\t", format(farenheight, '.2f')) # Print the relevant output

conversion() # Call the function in question
