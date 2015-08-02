# Write a program that contains course numbers and the room numbers for when the courses meet.
# The key-value pairs should look like the following:
{'CS101': '3004', 'CS102': '4501', 'CS103':'6755', 'NT110': '1244', 'CM241': '1411' }
# The program should create a dictionary that adds the following new values 
{'CS101': 'Haynes', 'CS102': 'Alvarado', 'CS103':'Rich', 'NT110': 'Burke', 'CM241': 'Lee' } # New Instructors
# The program should also add to the dictionary the values of the meeting times
{'CS101': '8:00am', 'CS102': '9:00am', 'CS103':'10:00am', 'NT110': '11:00am', 'CM241': '1:00pm' } # New Instructors
# Allow the user to enter a course number, and return the relevant room number, instructor, and meeting time

def  main(): # Create the main function
	
	# Create the initial course dictionary
	course = {'CS101': '3004', 'CS102': '4501', 'CS103':'6755', 'NT110': '1244', 'CM241': '1411'} # Dictionary of potential courses
	
	print("Welcome to the course information system for The Univeristy of Newt")
	print("The following courses are currently within the course information system:\n", course_listing(course))
	print("") # Print a blank line

	prompt = input("Would you like to search for a course number in the system? Please enter Y or N ")
	if prompt == "Y":
		#Allow the user to search for a room number
		request = input("Please enter the course number that you would like to find: ") # Request the course
		print("The course that you requested,", request, " is being held in the following room:", course[request])
	else:
		print("You do not want to search for a course at this time. Please continue browsing!")
	
	# Change each of the keys in the dictionary to a list
	for key in course.keys():
		course[key] = [course[key]] # Make each of the course keys a list

	# Allow the user to add names to the dictionary. For that, need to make each value a list
	prompt = input("Would you like to add names to the course dictionary? Please enter Y or N ")
	if prompt == "Y":
		print("Please update all courses in the dictionary with the correct instructor!")
		for a  in course:
			print("The class you are currently editing in the dictionary listing is", a)
			new_instructor = input("Please enter the instructor name for this class:" )
			course[a].append(new_instructor)
	else:
		print("You do not choose to update names in the course dictionary at this time. Please continue browsing!")
	
	# for key in course.keys(): # Note that this approach could be used if we skipped the step above
		#print("The next class in the dictionary listing is", key)
		#new_instructor = input("Please enter the instructor name for this class:" )
		#course[key] = [course[key], new_instructor] # Make each of the course keys a list

	# Allow the user to add class times to the dictionary. This assumes that lists holding values for the previous keys were created
	prompt = input("Would you like to class times to the course dictionary? Please enter Y or N ")
	if prompt == "Y":
		print("Please update all courses in the dictionary with the correct class time!")
		for b in course:
			# Note that a refers to the key for the specific course and course[a] refers to the values for the specific course
			print("The class you are currently editing in the dictionary listing is", b)
			class_time = input("Please enter the time that this class takes places at:" )
			course[b].append(class_time)
	else:
		print("You do not choose to update names in the course dictionary at this time. Please continue browsing!")

	# Allow the user to search again for a course and get all its properties
	print("")
	print("Welcome back to the course search engine!")
	print("The following courses are currently within the course information system:\n", course_listing(course))
	prompt = input("Would you like to search for a course number in the system? Please enter Y or N ")
	if prompt == "Y":
		new_request = input("Please enter the course number that you would like to find: ") # Request the course
		print("This course is being held in the following room:", course[new_request][0])
		print("The course is currently being taught by the following instructor:", course[new_request][1])
		print("This course starts at the following time every day:", course[new_request][2])
	else:
		print("You do not choose to search for a course in the course dictionary at this time. Have a great day!")
	
def course_listing(course): # Pass in the current dictionary of courses
	course_list = [] # Create an empty list of courses to hold the course listing data
	#for a in course: # Loop through all the potential courses in the course database
	#	course_list.append(a) # Append the created loop
	#return course_list # Return the course list to the initial function
	
	# Note that this is an alternative method that lists the keys in the course dictionary
	for key in course.keys(): # Find the keys that are in the course listing
		course#print(key)
		course_list.append(key) # Append the created loop
	return course_list # Return the course list to the initial function

main() # Call the main function
