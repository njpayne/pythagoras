# Write a program that uses nested loops to draw the following pattern (or make it sophisticated so that
# it can draw a pattern specified in the same orientation)
# *******
# ******
# *****
# ****
# ***
# **
# *

y = int(input("What is the target height of the unit that you are drawing? "))

for x in range(y + 1, 1, -1): # This produces an iterable containing the integers 0 to 6
	for z in range(x - 1): # This prints the number of columns of the object
                # Note that the (- 1) on the section above ensures that the last row has only 1 column (not 2)
		print("*", end='') # Causes one to print the ***
	print() # This prints the number of rows of the object & makes a slot in memory

		
