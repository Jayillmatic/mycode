#! /usr/bin/env python3

################################################################
#cels_list is the LIST of Celius Temperatures
#fahr_list is the LIST of Fahrenheit temperatures
###############################################################
cels_list = [-2, 0, 5, 10, 15, 25, 32, 38, 40]
fahr_list = [] #empty list

###############################################################
#Use a FOR loop to access each item in the list
#Find the corresponding Fahrenheit temperature.
#Append it to the fahr_list
###############################################################
for c in cels_list:
	f_temp = c * 1.8 + 32.0
	fahr_list.append(f_temp)

print("The Celsius list: ", cels_list)
print("The Fahrenheit list: ", fahr_list)