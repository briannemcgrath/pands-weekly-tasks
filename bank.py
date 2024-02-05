#bank.py
#Prompt the user and read in two money amounts (in cent)
#Add the two amounts 
#Print out the answer in a human readable format with a euro sign and decimal point between the euro and cent of the amount 
#Author: Brianne McGrath 

amount1 = int (input("Please enter the first amount (in cents):"))
amount2 = int (input("Please enter the second amount (in cents):"))

#creating the two input prompts

total = amount1 + amount2

#creating the sum of the two inputs

answer = total / 100

#making the answer into a demical format 

print ("The sum of these is €",answer)
