# An object that is in motion is said to have kinetic energy. The formula for KE is
# KE = 1/2 m*v^2 .... KE is the energy in joules, m is the object's mass in kilograms
# and v is the object's velocity in meters per second
# Write a program that accepts an objects mass and velocity in meters per second
# and then returns the kinetic energy that the object has. Calculate this within a function
# that is called.

def energy():
	mass = float(input("Please enter the mass of the object in question: "))
	velocity = float(input("Please enter the velocity of the object in question (in m/s): "))

	print("The kinetic energy of your object is", 
		format(kinetic(mass, velocity), ".2f"),
		"joules!")

def kinetic(x,y): # Create the kinetic energy function
	ke = (1 / 2) * x * (y ** 2) # Calculate the kinetic energy of the object
	return ke # return the kinetic energy

energy() # Call the main function
