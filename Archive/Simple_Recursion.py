# Create a simple recursive function that prints the statement ("this is a recursive function")
# 5 times ...

def main():
	number = int(input("Please enter the number of times that you would like to see the message: "))
	message(number)

def message(x):
	if x > 0: # Note that I cannot use the while option here
		print("This is a recursive function!")
		message(x - 1)

main() # Call the main function
