# Write a program that asks the user to enter the amount he or she has budgeted for a month
# Then, write a program that prompts the user to enter expenses for the month and keep
# a running total. When the loop finishes (allow the user to terminate), the program should 
# display the amount the user is over or under budget.

def budget(): # Create the budget function
	import locale
	locale.setlocale( locale.LC_ALL, '' )

	budget = float(input("Please enter your total budget for the month: "))
	question = input("Would you like to enter an expense? ('y' or 'n') ")
	total = 0 # Keep track of your total spending
	num_of_purch = 0 # Keep track of the number of purchases

	while question != 'n':
		expense = float(input("Please enter the dollar amount of the expense: "))
		total = total + expense
		num_of_purch = num_of_purch + 1
		question = input("Would you like to enter another expense? ('y' or 'n') ")

	print("")
	print("The total that you spent during the month is", 
		locale.currency(total, grouping = True))
	print("You made a total of", num_of_purch, "purchases during the month!")
	print("You spent an average of",
		locale.currency(total / num_of_purch, grouping = True),
		"on each purchase!")

	# Check whether your spending is under or over budget (or on budget)
	if budget > total: 
		print("You are under budget by a total of", 
			locale.currency(budget - total, grouping = True))

	elif budget == total:
		print("You spent all of your budget (exactly)!")

	else:
		print("You are over budget by a total of",
			locale.currency(total - budget, grouping = True))

budget() # Call the budget function





