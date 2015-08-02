# The following program determines the sale price of an item
# Suppose a retail business is planning to have a storewide sale where prices of all items
# will be 20 percent off. Create a program to calculate the sale price of the item
# After relevant discounts have been taken

import locale #Note that the locale module opens access to the POSIX locale database and functionality
# Specifically, the locale module does data and time formatting
locale.setlocale( locale.LC_ALL, '' )

# Input the original price and the discount price
original_price = int(input('Please enter the original price of your item:'))
discount = int(input('Please enter the total percentage discount'))

# Calculate the sale price of the item
sale_price = (discount / 100) * original_price

# Print out the final price of the item
print('The price of your item before taxes is going to be:', 
	locale.currency( sale_price, grouping=True ))


