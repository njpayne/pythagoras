# there are three seating categories at a stadium. For a softball game, Class A seats cost $15,
# Class B seats cost $12, and Class C seats cost $9. Write a program that asks how many
# tickets for each class were sold, and then displays the amount of income generated from ticket sales

# Notice that I created global variables here which are used in each of the functions
class_a = int(input("Please enter the number of Class A seats that were sold: "))
class_b = int(input("Please enter the number of Class B seats that were sold: "))
class_c = int(input("Please enter the number of Class C seats that were sold: "))

def class_a_calc(class_a): # This is the class a tickets function
	import locale
	locale.setlocale( locale.LC_ALL, '' )

	total_a = class_a * 15
	print("The total sales generated from Class A seats was",
		locale.currency(total_a, grouping=True ))

def class_b_calc(class_b): # This is the class b tickets function
	import locale
	locale.setlocale( locale.LC_ALL, '' )

	total_b = class_b * 12
	print("The total sales generated from Class B seats was",
		locale.currency(total_b, grouping=True ))

def class_c_calc(class_c): # This is the class c tickets function
	import locale
	locale.setlocale( locale.LC_ALL, '' )

	total_c = class_c * 9
	print("The total sales generated from Class C seats was",
		locale.currency(total_c, grouping=True ))

def total_tickets(class_a, class_b, class_c): # This is the total tickets function
	import locale
	locale.setlocale( locale.LC_ALL, '' )

	total = (class_a * 15) + (class_b * 12) + (class_c * 9)
	print("The total value of all sales generated during the game was",
	locale.currency(total, grouping=True ))

# Call the functions that operate on the global variables
class_a_calc(class_a)
class_b_calc(class_b)
class_c_calc(class_c)
total_tickets(class_a, class_b, class_c)

