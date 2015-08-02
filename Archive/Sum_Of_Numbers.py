# Write a program with a loop that asks the user to enter a series of positive numbers.
# the user should enter a negative number to signal the end of a series. After all the positive
# numbers have been entered, the program should display their sum

print("The following program is an addition program that sums numbers.")
print("Please enter a negative number when you want to see the total sum!")

def summing():
	sum = 0 # This is the total sum for the series. Aggregation starts at 0
	x = float(input("Please enter the number that you would like to add to your series: "))

	while x >= 0:
		sum = sum + x # Add the number entered to the total that you have entered
		# Note that the line below repeats the value that was initially entered!
		x = float(input("Please enter the next number that you would like to add to your series: "))

	print(sum) # Print sum once the program exist (outside of the loop)

summing() # Call the summing function	