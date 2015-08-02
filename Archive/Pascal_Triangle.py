# Pascal's triangle is a triangular array of the binomial coefficients
# Create a function that outputs all arrays of binomial coefficients from 1 to n

def main(): # Define the main function
    h = int(input("Please enter the height of the triangle: ")) # Enter the height
    for i in pascal(h): # Loop through the height of the triangle
        print(i) # Print each row
                    
    choice = input("Would you like to create another triangle? (y/n): ")
    if choice == "y":
        main() # Call the main function
    else:
        print ("Thank you for using Pascal's Calculator!") # Send a good-bye message

def pascal(a): # This is the triangle function
    trianglevar = [[1]] # This is the initial list with a 1 inside it
    for i in range(1, a): # For loop for the elements in range 1 to a
        tempvar = [1] # This is a list with 1 element inside it
        
        for n in range(0, i-1): # Calculate the next number in the list
            tempvar.append(trianglevar[i-1][n]+trianglevar[i-1][n+1])
        
        tempvar.append(1) # Append the temporary list
        trianglevar.append(tempvar) #Append the list with 1 element inside it
    return trianglevar # Return the triangle

main() # Call the main function
