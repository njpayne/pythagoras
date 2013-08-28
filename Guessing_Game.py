# Write a program that allows a user to play a guessing game. 
# Pick a random number in between 1 and 100, and then prompt the user for a guess. 
# For their first guess, if it’s not correct, respond to the user that their guess was “hot.” 
# For all subsequent guesses, respond that the user was “hot” if their new guess is 
# strictly closer to the secret number than their old guess and respond with “cold”, 
# otherwise. Continue getting guesses from the user until the secret number has been picked.
# Also, let the user know how many guesses it took to get the number!

def main(): # Define the main function
	import random
	a = random.randint(1,100) # Generate a random number between 1 and 100

	print("Welcome to the guessing game program!")
	print("To play, keep entering a number until you guess the number!")
	print("") # Print a blank line
	
	guess = [] # Create a lists to hold the guesses
	num = int(input("Please enter an integer between 1 and 100: "))
	guess.append(num) # Append the list and add the guess to the list
	
	counter = 1 # Increase the conter since the person made a guess

	if num != a: # If the first guess is not equal to the random number
		print("You missed it! Guess again!") # Prompt the user for another guess
		num = int(input("Enter a new integer between 1 and 100: ")) # Ask for the next number
		guess.append(num) # Append the list and add the next guess to the list
		
		counter = counter + 1 # Add one to the counter

		while num != a: # While the guess is not equal to the random number
			if abs((guess[len(guess)-1] - a)) < abs((guess[len(guess) - 2] - a)):
				print("You are getting hotter (i.e. closer to the actual number)! Guess again!")
				num = int(input("Enter a new integer between 1 and 100: "))
				guess.append(num) # Append the list and add the next guess to the list
				# Note that abs(guess[len(guess) - 1]) is the value of the most recent guess
				# Note that abs(guess[len(guess) - 2]) is the value of the previous guess
				
				counter = counter + 1 # Add one to the counter
			
			else:
				print("You are getting colder (i.e. farther away from the actual number)! Guess again!")	
				num = int(input("Try and enter a new integer between 1 and 100: "))
				guess.append(num) # Append the list and add the next guess to the list

				counter = counter + 1 # Add one to the counter

		print("You got it! The random number was", a, "! Amazing work!") # Success message when they get it!
		print("That took you a total of", counter, "guesses to guess the number!")
		print("Below is the list of all guesses that you made!")
		print(guess)

	else: # If the first guess is equal to the random number
		print("That is amazing! You guessed the number on the first try! Incredible!")

main() # Call the main function
