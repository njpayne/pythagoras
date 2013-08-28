# A technician must check a substance's temperature every night. If the 
# temperature is greater than 102.5 degrees celcius, the technician must
# turn down the thermostat, wait 5 minutes, and then check the temperature again.
# Write a program that guides the technician through the process

def temperature():
	enter_temp = input("Would you like to test the temperature? (y = yes; n = no): ")

	while enter_temp == 'y':
		temp = float(input("Please input the temperature of chemical x: "))

		if temp < 102.5:
			print("The temperature of the current chemical is",
				format(temp, '.2f'))
			print("This temperature is less than 102.5")
			enter_temp = input("Please press 'y' if you would like to re-enter the temperature at the next testing period: ")
		
		else:
			print("The temperature of the current chemical is currently greater than 102.5")
			print("Please follow the following steps:")
			print("Turn the thermostat down!")
			print("Wait 5 minutes")
			print("Check the temperature again!")
			print("Once you are ready to re-enter the temperature, please click the 'y' button!")
			enter_temp = input("Please press 'y' to re-enter the temperature:")

temperature() #Call the temperature function
print("") # Print a space
print("Thank you for using the temperature control program! Have a great night!")
