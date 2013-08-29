# Write a class named Employee that holds the following data about an employee: 
# name, ID number, department, job title; Once you are completed, enter some employee information
# Susan Meyers, 47899, Accounting, Vice President;  Mark Jones, 39119, IT, Programmer; Joy Rogers, 81774, Manufacturing, Engineer
# Question ... Future thought ... How to dynamically change a class

class Employee: # Create a new class called the Employee clas to hold information about an employee
	"""docstring for Employee"""
	def __init__(self, name, ID, dept, title): # Class will hold a total of 4 items about each employee
		super(Employee, self).__init__()
		self.__name = name # Employee name
		self.__ID = ID # Employee ID
		self.__dept = dept # Employee dept
		self.__title = title # Employee title

	def set_name(self, name): # Mutator function
		self.__name = name # Employee name

	def set_ID(self, ID): # Mutator function
		self.__ID = ID # Employee ID

	def set_dept(self, dept): # Mutator function
		self.__dept = dept # Employee dept

	def set_title(self, title): # Mutator function
		self.__title = title # Employee title

	def get_name(self): # Accessor function
		return self.__name

	def get_ID(self): # Accessor function
		return self.__ID

	def get_dept(self): # Accessor function
		return self.__dept

	def get_title(self): # Accessor function
		return self.__title

	def __str__(self):
		return 'The employee name is: ' + self.__name + \
		'\nThe Employee ID is: ' + self.__ID + \
		'\nThe Employee Department is: ' + self.__dept + \
		"\nThe Employee's job title is: " + self.__title


		
