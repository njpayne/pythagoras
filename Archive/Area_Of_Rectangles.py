# Write a program that asks for the length and width of two rectangles.
# The program should tell the user which rectangle has the greater area, or
# if the area of the rectangles is the same

l_1 = float(input("Please enter the length of the first rectangle: "))
w_1 = float(input("Please enter the width of the first rectangle: "))
l_2 = float(input("Please enter the length of the second rectangle: "))
w_2 = float(input("Please enter the width of the second rectangle: "))

def area(w, x, y, z):
	area_1 = w * x
	area_2 = y * z

	if area_1 > area_2: # Rectangle 1 is bigger than rectangle 2
		print("The first rectangle that you entered has an area of",
			format(area_1, '.2f'),
			"squared. This area is bigger than the area of rectangle 2, which has an area of",
			format(area_2, '.2f'),
			"squared.")

	elif area_2 > area_1: # Rectangle 2 is bigger than rectangle 1
		print("The second rectangle that you entered has an area of",
			format(area_2, '.2f'),
			"squared. This area is bigger than the area of rectangle 1, which has an area of",
			format(area_1, '.2f'),
			"squared.")

	else: # Both rectangles are equal
		print("Both rectangles have an area of",
			format(area_2, '.2f'),
			"squared. This area is equal!")

print("") # Print a blank line for the function in question
area(l_1, w_1, l_2, w_2) # Call the area function
