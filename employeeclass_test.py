# Test the employeeclass using the following information
# Susan Meyers, 47899, Accounting, Vice President;  Mark Jones, 39119, IT, Programmer; Joy Rogers, 81774, Manufacturing, Engineer

import employeeclass # Import the employee class

def main(): # Create the main function
	employee_listing = [] # Create a general list to hold the employee information
	
	ask = input("Would you like to enter some new user information into the program? (y or n): ")

	while ask.lower() == 'y':
		na = input("Please enter the name of the user: ")
		emp_ID = input("Please enter the ID of the employee: ")
		dept = input("Please enter the department of the employee: ")
		title = input("Please enter the title of the employee: ")

		ask = input("Would you like to enter some more user information into the program? (y or n): ")

	user = employeeclass.Employee(na, emp_ID, dept, title) # Create the new employee object
	employee_listing.append(user) # Append each employee listing with the employee object

	counter = 1
	for x in employee_listing: # For each of the objects in the employee listing
		print("Here is the information for employee", counter)
		print("Employee Name: ", x.get_name()) # Get the employees name
		print("Employee ID:", x.get_ID()) # Get the employees ID
		print("Employee Department: ", x.get_dept()) # Get the employees department
		print("Employee Title: ", x.get_title()) # Get the employees title
		print("") # Print a blank space
		counter += 1 # Add one to the counter
	
main() # Call the main function
