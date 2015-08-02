# Write a program that allows a user to play a guessing game. 
# Pick a random number in between 1 and 100, and then prompt the user for a guess. 
# For their first guess, if it’s not correct, respond to the user that they missed their guess. 
# Continue getting guesses from the user until the secret number has been picked.

def main(): # Define the main function
	import random
	a = random.randint(1,100) # Generate a random number between 1 and 100

	print("Welcome to the guessing game program!")
	print("This program will allow you to see how many guesses it takes to guess a random number!")
	print("To play, keep entering a number until you guess the number!")
	print("") # Print a blank line
	
	num = int(input("Please enter an integer between 1 and 100: "))
	
	if num != a: # If the first guess is not equal to the random number
		print("You missed it! Let's try another guess!") # Prompt the user for another guess
		while num != a: # While the guess is not equal to the random number
			if num < a:
				print("You are too low. Guess again!")
				num = int(input("Enter a new integer between 1 and 100: "))
			else:
				print("You are too high")	
				num = int(input("Enter a new integer between 1 and 100: "))

		print("You got it! The random number was", a, "! Amazing work!") # Success message when they get it!

	else: # If the first guess is equal to the random number
		print("That is amazing! You guess the number on the first try! Incredible!")

main() # Call the main function