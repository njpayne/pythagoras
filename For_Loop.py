# Write a for loop that displays the following sets of numbers
# 10, 20, 30, 40, 50 ... 1000

for x in range(1,101): # This sets the range from 1 to 101 (Correspinding ot 10 to 1000)
	# note that range can be stated as (1, 101, 1); 1 = start, 101 = end, 1 = step
	x = x * 10 # Cycle through each number, where the default increment is 1
	print(x) # Print the x value each time



