# If you know the mass of an object in kilograms, you can calculate its weight
# in newtons with the following forumula: weight = mass x 9.8
# Write a program that asks the user to enter an object's mass, and then
# calculates its weight. If the object weighs more than 1,000 newtons, display
# a message indicating that it is too heavy. If the object weihs less than
# 10 newtons, display a message indicating that it is too light.

# Declare the global variable mass
mass = float(input("Please enter the total mass of the object (in kilograms): "))

def mass_convert(x): # Define the conversion function
	y = x * 9.8

	if y < 10:
		print("The current object's mass is too little to accurately determine its weight!")
	
	elif y < 1000:
		print("The weight of your object (in newtons), is",
			format(y, '.2f'),
			"newtons!")
	else:
		print("The current object's mass is too heavy to enable accurate weight measurement!")

print("")
mass_convert(mass) # Call the function
