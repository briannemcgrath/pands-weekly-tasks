#account.py
#Prompt the user to enter 10 digit account number 
#Output the account number with only the last 4 digits showing and the rest sensored with X
#Author: Brianne McGrath 

while True:
    #Prompt the user to enter their 10 digit account number.
    account_number =  input("Please enter your 10 digit account number:") 

    #Validating the input
    if len(account_number) == 10 and account_number.isdigit():
        #Replacing the first 6 digits with 'X' to secure the account number
        secure_account_number = 'X' * 6 + account_number[-4:]

        #Printing the secure account number
        print(secure_account_number)

        #Exit the loop since a valid account number has been entered
        break

    else:
        #Show an error message for an invalid input (not 10 digits long)
        print ("Your account number is invalid. Please enter your 10 digit account number:")