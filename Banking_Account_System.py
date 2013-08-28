# Create a micro program that simulates a bank account

class BankAccount: # Create a new class called Bank Account, which is the blueprint
	"""docstring for BankAccount"""
	def __init__(self, bal): # Initiate the self initializer method which will execute automatically
		self.__balance = bal # Note that the bal parameter will accept the account's starting balance as an argument
		# Note that above, the bal parameter amount is assigned to the object's __balance attribute

	def deposit(self, amount): # This method will make a deposit into the account
		self.__balance += amount # Balance will be increased once any amount is given

	def withdrawal(self, amount): # This method will make a withdrawal from the account
		if self.__balance >= amount:
			self.__balance -= amount # Balance will be decreased once any amount is given
		else:
			print("You current have insufficient funds in your account to make the requested withdrawal")

	def get_balance(self): # This get method returns the account balance
		return self.__balance # Note that the __str__ method returns a string indicating the objects state

	def __str__(self):
		return 'The balance is $' + format(self.__balance, ',.2f') # Returns the statement as well as actual balance

# import ... # Note that I could import this class information from another file and reference it accordingly
# Note that import bankaccount2 would refer to a file where the class is stored called bankaccount2.py

def main(): # Create the main function
	starting_balance = float(input("Please enter the starting balance of the bank account: ")) # Get the starting balance
	savings = BankAccount(starting_balance) # Create a new bank account object
	# Note that savings is what we have named this new BankAccount object

	# Deposit the users paycheck
	pay = float(input("How much money would you like to deposit? "))
	print("Thank you for your deposit. I will now deposit this amount into your bank account!")
	savings.deposit(pay) # Apply the deposit method to the savings function, which is a function within the class BankAccount
	print(savings) # Print the total balance in the savings account (note that the get balance is associated)

	# Withdraw an amount from the users paycheck
	cash = float(input("How much would you like to withdraw from your account? "))
	print("Thank you for making the request. I will now attempt to withdraw that from your account.")
	savings.withdrawal(cash) # Attempt to withdraw the requested amount from the savings account
	print(savings) # Print the total balance in the savings account which corresponds to the value of the object when queried

main() # Call the main function
