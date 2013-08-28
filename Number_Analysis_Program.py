# Design a program that asks the users to enter a serise of 20 numbers. 
# The program shouldstore the numbers in a list and display the following data:
# The lower number in the list, the highest, the total, and the average of the numbers in the list

def main(): # The main function
	
	many = int(input("How many numbers would you like to enter in your list? "))
	counter = 0 # Initialize the counter
	store = [] # Create an empty list to hold the numbers
	sum = 0 # Initialize an initial sum that will keep track of the of the list

	while counter < many:
		num = int(input("Please enter the first number: "))
		store.append(num)
		counter += 1

	# Calculate the summary data for the numbers in the list
	print("The minimum value in the list is:", min(store)) # Display the minimum number for the list
	print("The maximum value in the list is:", max(store)) # Display the maximum number on the list

	for i in range(0,len(store)): # The sum function for all the numbers in the list
		item = store[i] # Grab the ith item in the list called store
		sum += item # add item to the variable sum

	print("The sum of all the values in the list is:", sum)
	print("The average of all the values in the list is:" (sum / len(store)))

main() # Call the main function