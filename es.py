#es.py
#Write a program that reads in a text file and outputs the number of e's it contains.
#Assumptions: 
#The input file is a plain text file. 
#The program is intended to be run from the command line or terminal. 
#We want to count all occurrences of 'e' regardless of case sensitivity. 
#Author: Brianne McGrath 

#Import the sys module to access command line arguments
import sys 

def es(filename):
    try: 
        #Open the file in read mode 
        with open(filename, 'r') as file:
            #Read the content of file and count occurrences of 'e' (not case sensitive) 
            content = file.read()
            count_e = content.lower().count('e')
            return count_e
    #Error handling
    except FileNotFoundError: 
        print(f"Error: File '{filename}' not found.")
        return None
    except Exception as e:
        print(f"An unexpected error has occurred: {e}")
        return None

#Check if the script is being run as the main program
if __name__ == "__main__":
    #Check if a filename is provided as a command-line argument 
    if len(sys.argv) != 2:
        print("Please provide a filename as a command-line argument.")
        sys.exit(1)

#Get the filename from the commmand-line argument
filename = sys.argv[1]

#Count the occurrences of 'e' in the file using the 'e_count' function and printing the result. 
try:
    e_count = es(filename)

    if e_count is not None:
        print(f"The file '{filename}' contains {e_count} occurences of 'e'.")
except Exception as e: 
    #Handle unexpected errors during execution
    print(f"An unexpected error occurred: {e}")

