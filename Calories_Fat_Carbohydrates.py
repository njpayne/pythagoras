# Write a program that asks health club members for the number of fat grams and
# carbohydrate grams that they have consumed in a day. Note that
# Calories from fat = fat grams x 9; Calories from carbs = carb grams x 6

carbs = float(input("Please enter the total number of grams of carbs that you have consumed today: "))
fat = float(input("Please enter the total number of grams of fat  that you have consumed today: "))
cal_carbs = 0 # Since the variable is global in scope, need to declare it first
cal_fat = 0 # Since the variable is global in scope, need to declare it first

def carb(carbs):
	cal_carbs = carbs * 9
	print("The total grams of carbs that you have consumed today are", 
		format(cal_carbs, '.2f'),
		"grams!")

def fatty(fat):
	cal_fat = fat * 9
	print("The total grams of fat that you have consumed today are", 
		format(cal_fat, '.2f'),
		"grams!")

carb(carbs)
fatty(fat)

print("")
print("Always remember that a healthy mind = a healthy body!")
print("Higher, faster, stronger!")
