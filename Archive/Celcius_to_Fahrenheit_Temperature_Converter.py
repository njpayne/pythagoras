# Write a program that converts celcius temperature to fahrenheit temperature
# The formula is as follows: F = ((9/5)*C) + 32

print("The following program converts celcius temperature to fahrenheit")
celcius = float(input("Please enter the current temperature in celcius: "))

fahrenheit = ((9 / 5) * celcius) + 32 #Calculate the temperate in fahrenheit

print("You entered the following temperature in fahrenheit:", format(celcius,'.2f'), "degrees!")
print("This temperature converts to", format(fahrenheit,'.2f'), "degrees in fahrenheit!")
