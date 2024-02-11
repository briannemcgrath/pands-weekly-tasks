#account.py
#Prompt the user to enter 10 digit account number 
#Output the account number with only the last 4 digits showing and the rest sensored with X
#Author: Brianne McGrath 

account_number = str (input("Please enter your 10 digit account number:"))

#prompting the user to input account number 

n = 6 
replacement_str = "XXXXXX"
secure_account_number = account_number.replace(account_number[0:n], replacement_str, 1)

print (secure_account_number)

#Output shows the account number with the first 6 characters replaced by X's and then the remainder
#Need to come back and figure out how to do this when a number larger than 10 is input ** 