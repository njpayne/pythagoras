# Write a program that calculates the number of pitchers of lemonade 
# that can be made with certain raw materials. Ask the user to enter the 
# number of teaspoons of sugar and number of lemons necessary to make a pitcher 
# of lemonade. Follow this by asking the user the total number of 
# teaspoons of sugar and number of lemons that are available to make lemonade. 
# Use this information to calculate the number of full pitchers of 
# lemonade that can be made and also print out the leftover 
# ingredients (number of teaspoons of sugar and lemons) after those pitchers have been made.

import math # Import the math library

def main(): # Define the main function
	print("The following program calculates the number of pitchers required to make ")
	print("Note that 1 pitcher typically requires 3 lemons and 24 teaspoons of sugar")
	# sugar_req = int(input("Please enter the number of teaspoons of sugar necessary to make 1 pitcher: "))
	# lemons_req = int(input("Please enter the number of lemons required to make 1 pitcher: "))
	sugar_req = 24 # I made this assumption to make beta testing easier
	lemons_req = 3 # I made this assumption to make beta testing easier

	# Determine what is in your pantry
	sugar_pantry = int(input("How many teaspoons of sugar do you have in your pantry? "))
	lemons_pantry = int(input("How many lemons do you currently have in your pantry? "))

	pitchers_sugar = sugar_pantry / sugar_req # Calculate the number of possible pitchers from sugar
	pitchers_lemons = lemons_pantry / lemons_req # Calculate the number of possible pitchers from lemons

	# Determine which measurement is the limiting reagent
	if math.floor(pitchers_sugar) < math.floor(pitchers_lemons): # Sugar is the limiting reagent
		sugar_leftover = sugar_pantry - (math.floor(pitchers_sugar) * sugar_req)
		sugar_used = math.floor(pitchers_sugar) * sugar_req
		
		# Sugar determines how many pitchers were made; thus, we use pitchers_sugar in the calculation
		lemons_leftover = lemons_pantry - (math.floor(pitchers_sugar) * lemons_req)
		lemons_used = math.floor(pitchers_sugar) * lemons_req # Depends upon the amount of sugar used 

		# Feed the variables into the printing function which prints the output (removes duplication)
		printing(sugar_used, sugar_leftover, lemons_used, lemons_leftover, math.floor(pitchers_sugar))
		
	else: # Lemons is the limiting reagent; pitchers_lemons < pitchers_sugar
		sugar_leftover = sugar_pantry - (math.floor(pitchers_lemons) * sugar_req) # Lemon constraint determines sugar left
		sugar_used = math.floor(pitchers_lemons) * sugar_req # Lemon constraint determines sugar used
		
		# Sugar determines how many pitchers were made; thus, we use pitchers_sugar in the calculation
		lemons_leftover = lemons_pantry - (math.floor(pitchers_lemons) * lemons_req)
		lemons_used = math.floor(pitchers_lemons) * lemons_req # Depends upon the amount of sugar used 

		# Feed the variables into the printing function which prints the output (removes duplication)
		printing(sugar_used, sugar_leftover, lemons_used, lemons_leftover, math.floor(pitchers_lemons))

def printing(a, b, c, d, e): # Create a universal printing function which handles the variables to be printed
	print("") # Print a blank space
	print("You used a total of", a, "teaspoons of sugar!")
	print("You have a total of", b, "teaspoons of sugar leftover!")
	print("You also used a total of", c, "lemons!")
	print("You have a total of", d, "lemons leftover!")
	print("Using these ingredients, you were able to make a total of", e, "pitchers of lemonade!")

main() # Call the main function
