# The following program asks for the users personal information and then displays it back to the user

name = input('Please enter your name: ')
city = input('Please enter the name of the city you currently live in: ')
province = input('What province is that city in? ')
telephone = input('What is your home phone number? ')
college_major = input('What is your current college_major? ')

# Return back the information to the user
print('Thank you for entering your information!', name)
print('I see that you currently live in', city,',','!')
print('The best number to reach you appears to be', telephone)
print("It's also cool that we both have the same college major, which is", 
	college_major)
print('Have a great day!')
