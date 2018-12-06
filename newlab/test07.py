#! /usr/bin/env python3

###########################################
#a_list is the Original List
#b list is a similar list, with different order
###########################################
a_list = [1, 2, 3, 4]
b_list = [4, 3, 2, 1]

print("List A: ", a_list)
print("List B: ", b_list)
print()					# This is simply printing an empty line

##########################################
#Show that the LIST Order matters.
#a_list is NOT EQUAL to b_list
##########################################
if (a_list != b_list):
	print("a_list is NOT EQUAL to b_list.")

##########################################
#Modify LIST a_list
#Add the item 5 to the end of the list
#########################################
a_list.append(5)

print("The modified list using the APPEND: ", a_list)