# Write a program that converts the distance in kilometers to miles

# Get the relevant information from the user
k = float(input("Please enter the distance that you plan to run (in kilometers): "))

# Define the mph to k conversion function
def conversion(k):
	m = k * 0.6214
	print("You are planning to run", k, "kilometers on your next run!")
	print("This is the equivalent of running", m, "miles!")
	print("")
	print("Have a great run!")
	
# Call the main function
conversion(k)
