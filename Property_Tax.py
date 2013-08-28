# A county collects property taxes on the assessment value of property, which is 60 percent of the
# property's actual value. The property tax is then 64 cents for each $100 of the assessment value

acre = float(input("Please enter the total projected value of your property: "))

def property(acre): # Create the property function
	import locale
	locale.setlocale( locale.LC_ALL, '' )

	assessment_value = acre * 0.6 # Calculate the total assessment value
	tax = 0.64 * (assessment_value / 100)
	print("Based on our calculation, the total assessment value of your property is", 
		locale.currency(assessment_value, grouping=True )) # Print format = currency
	print("Additionally, the total property tax that you owe for your property is", 
		locale.currency(tax, grouping=True )) # Print format = currency

property(acre) # Pass the input value to the property function
	
	
