# Refer back to the World Series text file. Create a program that reads in a text file and creates a 
# dictionary in which the keys are the names of the teams and each key's associated value is the number
# of times that the team has won the world series (could do this for the Superbowl also)
# Ask the use for the year and display the team that won the world series (as well as the total
# Number of times that they won the world series in total

def main():
	superbowl_db_list = [] # Create an empty list to hold the superbowl winners
	winners = [] # Generate a new list that includes only the winners
	superbowl_db = {} # Create a blank dictionary that will eventually be populated

	superbowl = open('Superbowl_Winners.csv', 'r')
	for lines in superbowl: # For each of the lines in the superbowl file
		lines = lines.rstrip('\n') # Strip off the new line indendation for each line
		lines = lines.split(',') # Split the values within the .csv using the lines.split functionality
		superbowl_db_list.append(lines) # Append the list with the correct lines
		
	superbowl.close # Close the superbowl file

	#for x in range(0,8): # Review the initial 9 items on the list
	#	print(superbowl_db_list[x]) # Print each of the various list items in the superbowl_db_list

	# Without lines = lines.split(','), we get
	#Year,No.,Winner,Opposition,Score,Venue
	#2013,XLVII,Baltimore Ravens,San Francisco 49ers,34-31,New Orleans
	#2012,XLVI,New York Giants,New England Patriots,21-17,Indianapolis
	#2011,XLV,Green Bay Packers,Pittsburgh Steelers,31-25,Texas

	# With lines = lines.split(','), we get
	#['Year', 'No.', 'Winner', 'Opposition', 'Score', 'Venue']
	#['2013', 'XLVII', 'Baltimore Ravens', 'San Francisco 49ers', '34-31', 'New Orleans']
	#['2012', 'XLVI', 'New York Giants', 'New England Patriots', '21-17', 'Indianapolis']
	#['2011', 'XLV', 'Green Bay Packers', 'Pittsburgh Steelers', '31-25', 'Texas']

	for a in superbowl_db_list[1:]: # For each of the items in the superbowl listing
	# Note that the [:1] in the for loop strips off the first row values, if the first row has headers
		#print(a[0]) # Year 
		#print(a[1]) # No.
		#print(a[2]) # Winner
		#print(a[3]) # Opposition
		#print(a[4]) # Score
		#print(a[5]) # Venue
		winners.append(a[2]) # Append the table of winners to the winners list (need to exclude the first row)
		# Can I create a dictionary that specifies the key at (a[0]), and the first value as a[1]) ???
		superbowl_db[a[0]] = [a[1],a[2],a[3],a[4],a[5]] # Populate the empty dictionary with relevant values

	#print(superbowl_db) # Print a copy of the superbowl dictionary
	#print(winners) # Print the new list which includes only the winners

	query = input("Please enter a year from 1967 until today to see who won the superbowl that year: ") # Get input as string
	if query in superbowl_db:
		answer = superbowl_db[query]
		print("You are looking for information on the superbowl that took place in", query)
		print("This game was referred to as superbowl", answer[0])
		print("In this game, the", answer[1], "beat", answer [2], "by a score of", answer[3], "!")
		print("This game took place in", answer[4])
		print("Since 1967,", answer[1], "has won the superbowl a total of", winners.count(answer[2]), "times." )
		# note that winners.count(answer[2]) counts the number of times that answer[2] occurs in the relevant list
	else:
		print("I am sorry, but you entered a year in which the superbowl was not held.")
		
main() # Call the main function
