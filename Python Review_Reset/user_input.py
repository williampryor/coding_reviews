#Prompt the user to input something via print statements and variables

#ask for the user for their name
#adding str to the beginning of the statement locks the 
#user input to a string type only
your_first_name = str(input("What is your name? "))

#ask the user how many months they have coded
user_months_coded = int(input("How many months have you been coding? "))

#print the output of the stored input variables to test code so far
print(f"Your name is {your_first_name} and you have been coding for {user_months_coded} months.")

#Ask for another user's name
user_2_name = str(input("What is your friend's name? "))

#Ask the 2nd user how many months they have coded
user_2_months_coded = str(input("How many months has your friend coded? "))

#Print your friend's name and how long 
# they have been coding to test this code so far
print(f"Your friend's name is {user_2_name} and they have been coding for {user_2_months_coded} months.")

