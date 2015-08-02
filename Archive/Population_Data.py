# The file USPopulation.txt contains the list of the population, in thousands of the United States
# during the years 1950 and 1990. Create a program that reads in the lists content and then
# displays 1) The average annual change in population during that time period
# 2) The year with the greatest increase in population during that period
# 3) The year with the smallest increase in population during that time period

def population(): # Create the population function
	
	print("The following code models US population change year over year from 1950 to 1990.")

	population = open("USPopulation.txt", 'r') # Open the population file
	pop = [] # Create an empty list to hold the population data
	change = [] # Create an empty list to hold the percentage change data
	
	for lines in population: # Run through all the lines in the population data file
		lines = lines.rstrip('\n') # Strip off the line breaks
		pop.append(lines) # Append the revised population data set

	population.close() # Close out the population txt file

	pop = [int(i) for i in pop] # Convert all the values in the pop list to integers
	# print(pop) # For error checking

	for x in range(0,len(pop)-1):
		increment = (pop[x + 1] - pop[x])
		change.append(increment)
	# print(change) # For error checking

	total = 0 # Create an initial counter
	counter = 0 # Create an initial counter
	for a in change: # For the change list
		total += a # Add each new value to the total
		counter += 1 # add one to the counter

	# Find the average annual change in population
	print("The average annual change in population from 1950 through 1990 was", 
		format((total / counter),'.2f')) # Format the output using 2 decimal places

	min_change = min(change) # The index of the minimum of the change list
	change.index(min_change)
	print("The years which had the lowest change between them were", 
		(1950 + change.index(min_change) + 1),
		"and",
		(1950 + change.index(min_change)))
	print("The population in these two years was",
		change[(change.index(min_change))],
		"and",
		change[(change.index(min_change) - 1)],
		"respectively!")
	
	max_change = max(change) # The index maximum of the change list
	change.index(max_change)
	print("On the other hand, the years which had the maximum change between them were", 
		(1950 + change.index(max_change) + 1),
		"and",
		(1950 + change.index(max_change)))
	print("The population in these two years was",
		change[(change.index(max_change))],
		"and",
		change[(change.index(max_change) - 1)],
		"respectively!")

population() # Run the population function
