#weekday.py
#Write a program that outputs whether or not today is a weekday.
#Author: Brianne McGrath

import datetime

def is_weekday():
#Get the current date 
    today = datetime.datetime.now().weekday()

#Check to see if today is a weekday (Monday - Friday)
    if today < 5:
        return True
    else:
        return False
    
if is_weekday():
    print("Yes, unfortunately today is a weekday.")
else: 
    print("It is the weekend, yay!")

#Print statements to let us know if it's the weekend (yay) or not!