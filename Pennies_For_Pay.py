# Write a program that calculates the amount of money a person would earn over a period of time
# if their salary is one penny for the first day, two pennies for the second day, and continues
# to double each day. The program should ask the user for the number of days. Display a table showing
# what the salary was for each day, and then show the total pay at the end of the period.
# The output should be displayed in a dollar amount.

def pennies():
	x = int(input("Please enter the number of total days that you wish to count: "))

	print("")
	print("Days\tRate\tCum_Salary") # Print the header for the table
	print("--------------------------") # Print the line under the header

	total = 0 # Initialize the counter
	rate = 0.01 # Create a global constant for the initial payment

	for x in range(1, x + 1, 1):
		total = total + rate # Calculate the total cumulative salary
		print(x, "\t", rate, "\t", format(total, '.2f'))
		rate = rate * 2 # Double the initial payment

	import locale
	locale.setlocale( locale.LC_ALL, '' )

	print("") # Print a space
	print("The cumulative total that you have made after counting", x, 
		"days is", 
		locale.currency(total, grouping=True))

pennies() # Call the pennies function

	

