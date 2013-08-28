# Write a for loop that displays the total of the series
# 1/30 + 2/29 + 3/28 + .... 29/2 + 30/1

def counter():
	total = 0 # Initialize the accumulator variable outside of the loop

	# Print the table headings
	print('Num\tDenom\tValue\tCumSum')
	print('--------------------------------------------------')

	for x in range(1,31):
		unit_value = x / (31 - x) # This represents the individual value at each step in the series
		numerator = x
		denominator = 31-x
		total = total + unit_value # This calculates the runnning total
		print(numerator, '\t', denominator, '\t', 
			format(unit_value, '.2f'),
			'\t', 
			format(total, '.2f')) # Fill all relevant values into the table
		
counter() # Initialize the counter function
