# Write a while loop that lets the user enter a number. The number should be multiplied by 3
# The loop should iterate as long as the product is less than 200

print("The following program shows the product of a number times 3.")
print("Once a number is entered, the loop will iterate")
print("This loop will keep iterating as long as the product is less than 200")
number = int(input("Please enter a number that you would like to iterate from: "))

def multiplier(x):
	total = 0 # Define an initial value which counts the squares

	print("Number\tProduct\tCumSum") #Print the table header
	print("---------------------------")

	while x * 3 < 200:
		product = x * 3 # Calculate the product of the number entered
		x = x + 1 # Add one to the value of the number entered
		total = total + product # Add the value of the product to the cumsum
		print(x, "\t", product, "\t", total) # Print out the number and the product

print("") # Print a space before calling the function
multiplier(number) # Call the function to initiate the program
