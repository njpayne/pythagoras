# Design a program that lets the users enter the total rainfall for each of 12 months into a list.
# The program should calcualte and display the total rainfall for the year, the average monthly rainfall,
# and the mounts with the highest and lowest amounts

def main(): # Define the main function
	months = int(input("How many months will you be entering values for? "))
	rain = [] # Create an empty list that will hold the rainfall data
	print("You are going to enter values for", months, "months!")

	counter = 1 # Define the initial counter as counter = 1
	while counter <= months: # Create the while loop that is conditional on the counter
		num = int(input("Please input an integer value for each of the average monthly rainfalls: "))
		rain.append(num) # Append the rain list using the num variable
		# Note that lists are mutable, which means they can be changed
		counter += 1 # Add one to the counter (Could also use counter = counter + 1)

	print("You entered the following values:", rain) # Print the list rain
	rain[len(rain) - 1] = 9 # Exchange the last variable of the list for a new variable

	# Summary Statistics
	print("The length of the rainfall array is", len(rain)) # The length of the rain array
	print("The rainfall array, printed without the first 2 values, looks like this:", rain[2:])
	
	#Search for the value 3 in the list
	print("")
	search = int(input("Please enter the value that you want to search for: "))
	if search in rain: # Search for the value using the in function
		print("The number", search, "is in your list!") # The number is in the list
	else:
		print("The number you are looking for is not in your list!") # The number is not in the list
	
	# Print the maximum value on the list
	print("The maximum value on the rain list is", max(rain), "!")
	# Print the minimum value on the list
	print("The minimum value on the rain list is", min(rain), "!")
	
	# Insert a number in the list
	rain.insert(len(rain), 7)
	
	# Calculate the total of all months of rain

	print("Entry\tMonthly\tCumulative") # Print the table header
	print("--------------------------------")
	sum = 0 # Create an initial sum counter
	for x in rain: # Loop over the total number of entries within the rain list
		sum = sum + x # Add the value of x to the sum
		print(rain.index(x) + 1,"\t",x,"\t", sum)
		# rain.index(x) returns the index number of the value x from the rainfall list

	print("The total rainfall that accumulated during that period was equal to", sum, "!")
	print("The average rainfall that accumulated during that same period is equal to", sum / len(rain), "!")
		
main () # Call the main function

