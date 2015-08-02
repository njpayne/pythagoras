# The following function displays 5 random numbers between 1 and 100
import random # Important the random library

def main():
	print("Count\tRandom_Num") # Generate the table headers
	print("----------------------") # Generate the table main line

	for count in range(5): # Create the for loop
		number = random.randint(1,100) # Determine the random number
		print(count + 1, "\t", number) # Print the number of the random number

main() # Call the main function
