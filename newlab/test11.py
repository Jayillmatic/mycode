#! /usr/bin/env python3

my_num = 1234.56789
my_pi = 3.1415926535

print("My number is: ", my_num)
print("The value of pi: ", my_pi)

##################
#Format to 4 decible places
#Note that you dont need the 0 before the .2f
##################
print(format(my_num, '0.4f'), "Print using 2 decimal places")
print(format(my_num, '.4f'), "Also print using 2 decimal places")
print("NOTE that it rounded my results! ! !")
print()

#Format to only 1 decimal place
print(format(my_num, '.1f'), "Also print using 1 decimal places")
print("NOTE that it rounded my results! ! !")

#Format PI from 10 decimal places to 6 decimal places
print(format(my_pi, '.6f'), "Also print using 6 decimal places")
print("NOTE that if rounded my results ! ! !")