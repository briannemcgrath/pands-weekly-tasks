#Write a program that takes a positive floating-point number as input and outputs as approximation of its square root.
#Author: Brianne McGrath 

def sqrt(number):
    #Inital guess for the square root.
    guess = number / 2

    #Iterate until a good approximation is achieved. 
    #Applies Newton's method until the approximation is within the smallest tolerance.
    while abs(guess * guess - number) > 1e-10:
        guess = 0.5 * (guess + number / guess)

    return guess 

while True:

    i = float(input("Please enter a positive number:"))
    #Prompting the user toe enter a positive number. 

    if i <= 0:
        print("Please enter a positive number!")
    #Checking if the number is positive and if not, this error message is printed. 
        
    else:
        #Calculate and show the square root (approx)
        answer = sqrt(i)
        print(f"The square root of {i} is approx: {answer}")
        break #Exit the loop if a positive number is entered. 
