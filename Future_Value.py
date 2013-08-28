# Let us create a program that calculates the future value of an annuity based on an investment
# Made today for that annuity. The formula used to make this calculation is
# PV(1 + r)^2 = FV, where PV = present value, FV = future value, and r = the relevant rate

import locale #Note that the locale module opens access to the POSIX locale database and functionality
# Specifically, the locale module does data and time formatting
locale.setlocale( locale.LC_ALL, '' )

# Get the required variable
PV = float(input('Please enter the amount that you would like to invest today: '))
r = float(input('Please enter the interest rate you hope to attain for your investment: '))
n = float(input('Please enter the number of years that you hope to keep your investment: '))

# Calculate the future value of the annuity
# Remember to convert the rate to a percentage
FV = PV * ((1 + (r/100)) ** n)

# Return the results of that calculation to the user
print('The projected future value of your investment is:', 
	locale.currency( FV, grouping=True ))
