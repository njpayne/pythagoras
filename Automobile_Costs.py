# Write a program that asks the user to enter the monthly costs for the following expenses incurred
# from operating their automobile: Loan payment, insurance, gas, oil, tires, and maintenance
# The program should then display the total monthly cost of these expenses
# as well as the total annual cost of these expenses

# Get the relevant monthly information from the users
loan = float(input("Please enter the total amount of your monthly loan payment (in dollars): "))
insurance = float(input("Please enter the total amount of your monthly insurance payment (in dollars): "))
gas = float(input("Please enter the total amount of your monthly gas payment (in dollars): "))
oil = float(input("Please enter the total amount that you pay monthly for oil (in dollars): "))
tires = float(input("Please enter the total amount that you pay monthly for servicing your automobiles tires? (in dollars): "))
maintenance = float(input("Please enter the total amount that you pay monthly for maintenance (in dollars): "))

def monthly(loan, insurance, gas, oil, tires, maintenance):
	import locale
	locale.setlocale( locale.LC_ALL, '' )
	total_monthly = loan + insurance + gas + oil + tires + maintenance
	print("The total amount that you pay monthly for all automobile expenditures is",
	locale.currency(total_monthly, grouping=True ))

def annual(loan, insurance, gas, oil, tires, maintenance):
	import locale
	locale.setlocale( locale.LC_ALL, '' )
	total_annual = 12 * (loan + insurance + gas + oil + tires + maintenance)
	print("The total amount that you pay annually for all automobile expenditures is",
	locale.currency(total_annual, grouping=True ))

# Call both functions with the relevant parameters
print("")
monthly(loan, insurance, gas, oil, tires, maintenance)
annual(loan, insurance, gas, oil, tires, maintenance)
print("")
print("Thank you for shopping at Midas Muffler!")
