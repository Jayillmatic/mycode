#! /usr/bin/env python3

#Initialize your prompt string
prompt_name_msg = "Please enter your full name: "

######################################################
# Use the input function to get  the users's name
######################################################
user_name = input(prompt_name_msg)

######################################################
#ERROR CHECKING: Check that the user_name is not empty
######################################################
while (user_name == ''):
	#prompt the user again for thier name
	user_name = input(prompt_name_msg)
#END of the while loop, for the USER-NAME initialization

######################################################
# Print out a statement using the user_name variable
######################################################
print()
print('Welcome to the wonderful world of python,' , user_name)
print()