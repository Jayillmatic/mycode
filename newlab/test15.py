#! /usr/bin/env python3

sl = "%to,two,too!"
print(sl)

# This illustrates more string slicing
print(sl[0])

#This shows the last character in the string
print(sl[-1])

#This gets the first three characters in the string
#This includes indexes 0 to 2. IOt does not include index 3
print(sl[:3])

#This starts at index 7 and goes to the end of the string
print(sl[7:])	#This should print out the string', too!'

#This starts at index 3 and goes to index 7 (Does NOT include index 8)
print(sl[3:8]) 