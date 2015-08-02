# Create a sub program to test the car class

import carclass # Import the car classs

def main(): # Create the main function
	year = input("Please enter the year of the automobile: ")
	make = input("Please enter the make of the automobile: ")
	model = input("Please enter the model of the automobile: ")

	vehicle = carclass.Car(year, make, model)

	print("") # Print a blank space
	print("The vehicle was made inthe following year: ", vehicle.get_year())
	print("The make of the vehicle is a: ", vehicle.get_make())
	print("The model of the vehicle is a: ", vehicle.get_model())

main() # Call the main function
