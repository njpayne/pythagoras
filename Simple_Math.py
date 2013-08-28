# The following program demonstrates some simple math
# Ask the user for their current salary and annual bonus
# Then, return the compensation for that value

salary = float(input('Please enter your current salary: '))
bonus = float(input('Please enter the bonus you received last year: '))

total_compensation = salary + bonus #Calculate the total of salary + bonus

import locale #Note that the locale module opens access to the POSIX locale database and functionality
# Specifically, the locale module does data and time formatting
locale.setlocale( locale.LC_ALL, '' )

print('Thank you for entering your salary and bonus for the 2012 fiscal year!')
print('Based on our calculations, your total compensation for 2013 was', 
	locale.currency( total_compensation, grouping=True ))

