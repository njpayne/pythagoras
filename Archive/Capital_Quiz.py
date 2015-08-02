# Write a program that creates a dictionary holding the US States as keys and the state capitals as values
# Create a random quiz that gives the user a state, and asks them to enter the correct capital

def capital(): # Create the main capital function
	import random # Import the random mathematics package
	country_db_list = [] # Create an empty list to hold the country information
	country_db = {} # Create an empty dictionary that holds the country information

	country = open('Country_List.csv', 'r') # Open up the capital cities listing
	for lines in country: # For each of the various lines in the country list
		lines = lines.rstrip('\n') # Strip off the new line indendation for each line
		lines = lines.split(',') # Split the values within the .csv using the lines.split functionality
		country_db_list.append(lines)

	country.close # Close the capital cities listing

	# Note that the headers for the each of the .csv columns are in the first cell in the country_db list
	# ['Common Name', 'Formal Name', 'Type', 'Capital', 'Currency Code', 'Currency Name', 'Telephone Code', 'Letter Code']
	#print(country_db_list) # to check the listing as necessary

	# Put the items from the list into a dictionary that has the Common Name as the Key
	for a in country_db_list[1:]: # For each of the items in the superbowl listing
	# Note that the [:1] in the for loop strips off the first row values, if the first row has headers
		country_db[a[0]] = [a[1],a[2],a[3],a[4],a[5],a[6]] # Populate the empty country dictionary with relevant values
	#print(country_db['Canada']) # Print the first item in the list to review the dataset header
	#print(country_db)

	query = input("Please enter the name of the country you are looking for: ")
	if query in country_db:
		answer = country_db[query]
		print("You are searching for information about", query,".")
		print("The capital of", query, "is", answer[2],".")
		print("The national currency in", query, "is called the", answer[4])
	else:
		print("I am sorry, but you entered a country that does not exist (or perhaps mis-spelled the country name).")

	ask = input("Would you like to play the capital city game? (Please type Y or N) ")
	if ask == "Y":
		print("Awesome!")
		real_answer = random.randint(1,len(country_db)) # Grab a random number that will be user to locate a key
		solution = random.choice(list(country_db.keys())) # This grabs a random key from the dictionary list
		
		print("The country that has been randomly selected is", solution, ".")
		guess = input("Please enter the capital city of this country: ")

		solution_list = country_db[solution] # Generate the list holding the values of all information required
		if guess != solution_list[2]:
			counter = 1
			while guess != solution_list[2]:
				print("Sorry, close but just not close enough!")			
				guess = input("Please enter the next guess: ")
				counter += 1 # Add 1 to the counter
			print("Amazing! You got it!")
			print("The capital of", solution, "is", guess)
			print("It took you a total of", counter, "guesses to get the correct answer. Keep practicing.")
		
		else:
			print("Amazing! You got it on your first try!")
			print("The capital of", solution, "is", guess)

	else:
		print("Sorry you did not want to compete!")
		print("Get your act together and come back when you are ready to play!")
	
capital() # Call the main capital function
