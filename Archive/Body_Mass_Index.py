# Write a program that calculates and displays a person's body mass index (BMI)
# A person's BMI is calculed with the following formula
# BMI = weight x 703 / height^2

w = float(input("Please enter your current weight (in pounds): "))
h = float(input("Please enter your current height (in inches): "))

def bmi(w, h):
	body = w * (703 / (h ** 2)) # Calculate the users BMI
	print("")
	print("Based on our calculation, your current BMI is: ", 
		format(body, '.2f'))

bmi(w, h) # Call the function to initiate the program
