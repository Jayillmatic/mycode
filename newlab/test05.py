#! /usr/bin/env python3

#a list is the Original List
a_list=  [1, 2, 3, 4]
print(a_list)
print()					# This simply prints an empty line(More Below)

# Priunt out the elements in the original list
print('Item 1 ion the list is: ', a_list[0]) #Stored at index 0
print('Item 2 ion the list is: ', a_list[1]) #Stored at index 1
print('Item 3 ion the list is: ', a_list[2]) #Stored at index 2
print('Item 4 ion the list is: ', a_list[3]) #Stored at index 3
print()

#########################################################################
#reversed_list is the Orignal_list, reversed
#...It starts at the last element of the list, which is indicated by -1
#...It steps backward through the list, which is also indicated by -1
########################################################################
reversed_list = a_list[-1::-1]
print('The Reversed list...')
print(reversed_list)
print()

print("Now using the FOR loop to maneuver the entire list")
for my_item in reversed_list:
	print(my_item)		#This will print the reversed list vertically
# END of the FOR loop