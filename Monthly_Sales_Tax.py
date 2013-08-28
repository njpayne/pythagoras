# A retail company must file a monthly sales tax report listing the total
# sales for the month, and the amount of state and county sales tax collected.
# The state sales tax rate is 4 percent and the county sales tax rate is 2
# percent. Write a program that asks the user to enter the total sales for
# the month. From this figure, the application should calculate
# and display the following:
# 1) Amount of county sales tax
# 2) Amount of state sales tax
# 3) The total sale tax (county plus state)

# Declare a global variable that asks for the total sales for the month
total_sales = float(input("Please enter the total amount of sales made during the last month: "))

def tax(total_sales): # Function will be used to calculated the various tax rates
	import locale # Import the locale
	locale.setlocale( locale.LC_ALL, '' ) # Set the locale for use within the function (locally)

	county_sales = total_sales * 0.02
	state_sales = total_sales * 0.04
	total_county_state = county_sales + state_sales

	print("")
	
	print("You spent a total of", 
		locale.currency(total_sales, grouping=True ), 
		" last month!")
	
	print("The total county sales tax that you owe is",
		locale.currency(county_sales, grouping=True ),
		"dollars!")

	print("The total state sales tax that you owe is",
		locale.currency(state_sales, grouping=True ),
		"dollars!")

	print("The total sales tax that you owe is",
		locale.currency(total_county_state, grouping=True ),
		"dollars!")

tax(total_sales) # Call the tax function
