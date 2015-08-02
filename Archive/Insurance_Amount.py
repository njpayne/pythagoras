# Many financial experts advise that property owners should insure their homes
# or buildings for at least 80 percent of the amount that it would cost to replace the structure.
# Write a program that asks the user to enter the replacement cost of a building and then
# displays the minimum amount of insurance he or she should buy for the property

import locale
locale.setlocale( locale.LC_ALL, '' )

# Get the relevant values from the user
replacement = float(input("Please enter the projected replacement cost of the building that you want to insure: "))

# Define the function
def insurance(replacement):
	minimum = replacement * 0.8
	print("Based on our calculations, the minimum amount of insurance that you should buy for your property is",
	locale.currency(minimum, grouping=True ))
	print("Would you like to purchase insurance now?")

# Call the main function
insurance(replacement)
