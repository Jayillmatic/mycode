#! /usr/bin/env python3

sl = "%to,two,too!"

##########################
#Strip various characters from the string
#NOTE this applies to only LEADING and TRAILING characters
##########################
s2 = s1.strip('%!') #Strip just the % and ! characters
s3 = s1.strip(",")  #Strip only the comma

print("s1:", s1)
print("s2:", s2)
print("s3:", s3)  #The commas are inside the string, so it doesnt fine them!

s$