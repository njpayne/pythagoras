# Assuming that there are not accidents or deliays, a car travels down the interstate
# using the following formula: distance = speed x time
# Write a program that asks the user for the distance travelled
# Then, report the distance that the car will travel in 5, 8, and 12 hours

speed = float(input("Please enter the speed that you will be driving your car (in kph): "))

distance_5 = speed * 5 # Calculate the distance the car travels in 5 hours
distance_8 = speed * 8 # Calculate the distance the car travels in 8 hours
distance_12 = speed * 12 # Calculate the distance the car travels in 12 hours

# Print out the total distance travelled
print("The total distance that the car travels in 5 hours is", format(distance_5, '.2f'))
print("The total distance that the car travels in 8 hours is", format(distance_8, '.2f'))
print("The total distance that the car travels in 12 hours is", format(distance_12, '.2f'))
