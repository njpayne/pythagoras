# Write a program that analyzes charge accounts. These accounts are stored in a list.
# The program should ask the user to enter a number, and then search through the list to
# validate whether the number is valid or not ... 

def account(): # Create the base account function
	charge = open('charge_accounts.txt', 'r') # Open the charge accounts files
	charge_account = [] #Create an empty list to hold the charge account numbers

	for lines in charge: # For each of the lines in the inputted charge account file
		lines = lines.rstrip('\n') # Strip remove the line breaks
		charge_account.append(lines) # Append the list

	charge.close() # Close the charge account folder

	num = input("Please enter the charge account number that you wish to search for: ")
	
	if num in charge_account:
		print("The account number you entered is a valid account number!")
	else:
		print("The account number that you entered is not a valid account number")

account() # Call the account function
