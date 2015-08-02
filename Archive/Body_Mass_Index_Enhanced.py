# A person's BMI is calculated using the following formula: BMI = weight x 703/height^2
# In this case, weight is the weight in pounds and height is measured in inches
# Write a program that calculates a persons BMI and then return a message
# telling them which weight class they are in. A peson's BMI is considered optimal
# if it is between 18.5 and 25. If the BMI is less than 18.5, the person is
# considered to be underweight. If the BMI value is greater than 25, the person
# is considered to be overweight!

weight = float(input("Please input your total weight (in pounds): "))
height = float(input("Please input your total height (in inches): "))

def conversion(x, y): # Define the conversion function
	BMI = x * 703 / (y ** 2)

	if BMI < 18.5:
		print("Your current BMI is", 
			format(BMI,'.2f'), 
			". This means that you are underweight!")

	elif BMI <= 25:
		print("Your current BMI is", 
			format(BMI,'.2f'), 
			". This means that you have an optimal BMI!")

	else:
		print("Your current BMI is", format(BMI,'.2f'), 
			". This means that you are overweight!")

print("") # Print a space before writing the final statement
conversion(weight, height) # Call the function in question
