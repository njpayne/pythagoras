# The following forumla can be used to determine the distance that an object falls
# due to gravity in a specific time period from rest: d = 1/2gt^2
# d = distance, g = gravity = 9.8 m/s^2, t = time in seconds that the object has been falling
# Write a program that determines the distance in meters that an object has fallen during
# the time interval. Call the function in a loop and return the values in a table where
# t = 1 - 25 seconds

def main(): # Create the main function
	print("Time\tDistance(m)") # Print the table headers
	print("-----------------") # Print the table main headers

	for x in range(1,25 + 1): # Create the for loop to cycle through the values
		print(x, 
		"\t", 
		format(distance(x), ".2f")) # Print the output which calls the distance function

def distance(t): # The distance calculation function
	d = 1 / 2 * 9.8 * (t ** 2)  # Note that the distance is in meters
	return d # Return distance in the function above

main() # Call the main function
