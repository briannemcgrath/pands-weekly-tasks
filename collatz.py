#collatz.py
#Prompt the user to enter any positive integer
#Outputs the successive values of the following: 
#At each each calculate the next value by taking the current value and if it is: 
#Even = Divide by two
#Odd  = Multiply by three and add one

i = int (input ("Please enter any positive integer:"))
#Prompts the user to input their positive integer 

while i !=1:

#Creating a loop that keeps running until the answer reaches one. 
#When it reaches one then the program is finished and we exit the loop. 
    
    if i % 2 == 0:
        i = i // 2
#If the number entered is even we divide it by two.
    else:
        i = (i * 3) + 1
#Otherwise we multiply the answer by 3 and add one.

    print ("Answer:", i)
print ("The Answer is now equal to one - the program has ended.")

#We print the answer and run a loop until the answer is one. Once it reaches one, the program will tell us and exits the loop. 