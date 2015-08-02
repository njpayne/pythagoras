# A fast freight shipping company charges the following shipping rates:
# 2 pounds or less = $1.10
# Over 2 pounds but not more than 6 = $2.20
# Over 6 pounds but not more than 10 pounds = $3.70
# Over 10 pounds = $3.80
# Write a program that asks the user to enter the weight of a package and then
# displays the shipping charges

# Define weight as a global variable
weight = float(input("Please enter the weight of the package that you would like to ship: "))

def shipping(x): # Create the shipping function
	import locale
	locale.setlocale( locale.LC_ALL, '' )

	if x <= 2: # Package is less than or equal to 2 pounds
		y = x * 1.10 
	
	elif x <= 6: # Package is between 2 pounds and 6 pounds
		y = x * 2.20

	elif x <= 10: # Pakage is between 6 pounds and 10 pounds
		y = x * 3.70 

	else: # Package is more than 10 pounds
		y = x * 3.80

	print("It will cost a total of", 
		locale.currency(y, grouping=True), 
		"dollars to ship your package!")

print("") # Print a blank line
shipping(weight) # Call the function in question
