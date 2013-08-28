# A painting company has determined that, for every 115 square feet of wall
# one gallon of paing and eight hours of labor will be required. The company
# charges $20.00 per hour for labor. Write a program that asks the user to
# enter the square feet of wall space to be painted and the price of the
# paint per gallon. The program should display:
# The number of gallons of paint required, the hours of labor required,
# the cost of the paint, the labor charges, and the total cost of the paint job

# Input global variables & then pass those variables to the function
wall = float(input("Please enter the total square feet of the wall space to be painted: "))
price = float(input("Please enter the total price per gallon of the paint you are purchasing: "))

def calculator(wall, price):
	import locale
	locale.setlocale( locale.LC_ALL, '' )

	gallons = (wall / 115) * 1 # Calculate the number of gallons required
	hours = (wall / 115) * 8 # Calculate the number of gallons required
	labor_cost = 20 * hours # Calculate the labor cost
	paint_cost = price * hours # Calculate the paint cost
	total_cost = paint_cost + labor_cost

	print("You will require a total of", 
		format(gallons, '.2f'),
		"gallons of paint to paint your wall!")

	print("It will take a total of", 
		format(hours, '.2f'),
		"hours of labor to paint your wall!")

	print("It will cost a total of", 
		locale.currency(labor_cost, grouping=True ),
		"dollars in labor to paint your wall!")

	print("It will cost a total of", 
		locale.currency(paint_cost, grouping=True ),
		"dollars in paint to finish painting your wall!")

	print("The total cost of the paint job will be", 
		locale.currency(total_cost, grouping=True ),
		"dollars!")

print("") # Print a blank line
calculator(wall, price)	
	


