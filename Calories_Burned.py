# Running on a treadmill you burn 3.9 calories per minute. Write a program taht uses a loop to display
# the number of calories burned after 10, 15, 20, 25, and 30 minutes

def calories():
	print("Minutes\tCalories")
	print("----------------------")

	for x in [10, 15, 20, 25, 30]: # Where x refers to the number of minutes run
		calories = 3.9 * x # Count the total calories burned in each minute
		print(x, '\t', format(calories, '.2f')) # Print the output

print("Program displays the total that you have burned running on a treadmill")
calories() # Call the main function

