#!/usr/bin/env python3
#Create a list
my_list = [ "192.168.0.5", 5060, "UP" ]
# First line should begin with zero (integer)
print("The first item in the list (IP): " + my_list[0] )
#Second line list ports
print("The second item in the list (port): " + str(my_list[1]) )
# Display state
print("The last item in the list (state): " + my_list[2] )
new_list = [ 5060, "80", 55, "10.0.0.1", "10.20.30.1", "ssh" ]
print("When i ssh into IP address (IP)", new_list[3], "or", new_list[4], "I am unable to ping ports", str(new_list[0:3]), )