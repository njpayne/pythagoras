# Write a program that reads a string from the user containin a date in the form mm/dd/yy
# It should print out the date formate in the form March 12, 2012

def dates(): # Create the date function
	print("Welcome to the date conversion tool!")
	time = input("Please enter a date in the format (mm/dd/yy) that you wish to convert: ")

	month = time[0] + time[1] # Determine the month by combining the two digits of the string
	date = time[3] + time[4] # Determine the date by combining the two digits of the string
	year = time[6] + time[7] # Determine the year by combining the two digits of teh string

	print("You entered the following date:", time)
	print("This is equivalent to the following date:",
		month_convert(month), date, year_convert(year))
			
def month_convert(a): # Pass the function month
	# Create a list holding all the months
	month_list = ["January", "February", "March", "April", "May", "June", "July",
	"August", "September", "October", "November", "December"]

	if a[0] == "0": # Check whether the first digit of the month is a zero
		look = a[1] # If the first digit is a zero, determine the month using the second digit
		return month_list[int(look) - 1] # Return the correct month from the list
	else:
		look = a # If the first digit is not a zero, use all of a to determine the month
		return month_list[int(look) - 1] # Return the correct month from the list

def year_convert(c): # Pass the function year
	year_beginning = "20"
	return year_beginning + c

dates() # Call the date function
