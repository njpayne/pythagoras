# Write a program that uses a loop to display a table showing the numbers 1 through 25 and their squares
# Note: Augmented the program by adding a cumulative total column that counts the cumulative sum
# of the squared values as they are calculated

def squares():
	print('Num\tSquare\tCumSum') # Print the initial table header for the 3 columns
	
	total = 0 # Start a cumulative total counting the cumulative sum of the squared values

	for x in range(1,26): # Input the range of the number
		square = x ** 2 # Calculate the square of the number
		total = total + square
		print(x, '\t', square, '\t', total)

squares() # Call the squares function

		