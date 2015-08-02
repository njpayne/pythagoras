# Write a program that allows the user to control the range of the values over which the
# loop runs (to calculate their squares). 

print("This program displays a list of numbers, their squares, and the cumulative sum!")
min = int(input("Please enter the value that you would your range to start with: "))
max = int(input("Please enter the value that you would your range to start with: "))

def squares(min, max):
	total = 0 # This is the initial value for the cumulative total
	print("Num\tSquare\tCumSum") # Print the table headers
	print("------------------------") # Print a line below the table header

	for x in range(min, max+1):
		square = x ** 2 # Calculate the square of the function
		total = total + square
		print(x, "\t", square, "\t", total)

squares(min, max) # Call the squares function
