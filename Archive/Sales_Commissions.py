# Create a program that calculates a series of sales commissions

def commissions():
	keep_going = 'y' # Make sure this assignment is done properly!

	while keep_going == 'y':
		
		import locale # Import the locale package
		locale.setlocale( locale.LC_ALL, '' )

		sales = float(input("Please enter the total sales amount: "))
		comm_rate = float(input("Please enter the total commission rate (eg. 6.25 = 6.25%): "))

		commission = sales * (comm_rate/100) # Calculate the total commissions

		print("The total commission is", # Calculate the total commissions
			locale.currency(commission, grouping=True))

		keep_going = input("Do you want to calculate another commission (enter y for yes!): ")

commissions() # Call the main function
print("")
print("Thank you for using the commission calculator!")

