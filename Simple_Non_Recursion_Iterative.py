# Rather than using a recursive approach, use an iterative approach to solve the problem
# originally posed in the iterative problem set

def main():
        num = int(input("Please enter the number of times that you would like to see the message: "))

        for x in range(num + 1, 1, -1):
                print("This is a recursive function!")

main() # call the main function
