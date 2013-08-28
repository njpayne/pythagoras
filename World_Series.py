# Import a file containing the names of all world series winners from 1903 through 2009
# Write a program that lets the user enter the names of a team and then displays the number of times
# that team has won the World series in the time period from 1903 to 2009

def world_series(): # Create the main world series function
	world = open('WorldSeriesWinners.txt', 'r') # Open the file and get ready to read it in
	world_series = [] # Create an empty list to hold the world series data

	for lines in world:
		lines = lines.rstrip('\n') # Strip off the line breaks
		world_series.append(lines) # Append the world list with the data from the .txt document

	name = input("What team would you like to search for? ")

	counter = 0 # Create an initial counter that the number of occurences of the name in question

	for x in range(0,len(world_series)):
		if name == world_series[x]:
			counter += 1
		else:
			continue # Skip over the non-occurences

	if counter == 0 : # Value was not found in the list
		print("I am sorry. The team you entered, the", name, ", have never won the world series!")
	else:
		print("The", name ," have won the world series a total of", counter, "times!")

world_series() # Call the world series function
