#!/usr/bin/env python3
proto = ['ssh', 'http', 'https']
print(proto)
print(proto[1])
proto.extend('dns') # this line will add 'd','n','s',to the end of our list
print(proto)
proto2 = [22, 80, 443, 53] # a list of common ports
proto.extend(proto2) # pass proto2 as an argumet to the extended method -- then print result
print(proto)
proto.append(proto2) # pass proto2 as an argumet to the extended method -- then print result
print(proto)
proto.remove(proto2) # remove proto2 as an argumet to the extended method -- then print results
print(proto)
proto.count(proto2)
print(proto)