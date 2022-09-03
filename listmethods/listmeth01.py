#!/usr/bin/env python3
proto = ["ssh", "http", "https"]
protoa = ["ssh", "http", "https"]
print("proto:", proto)
proto.append("dns") # this line will add "dns" to the end of our list
protoa.append("dns") # this line will add "dns" to the end of our list
print("appended proto:", proto)
proto2 = [ 22, 80, 443, 53 ] # a list of common ports
proto.extend(proto2) # pass proto2 as an argument to the extend method
print("proto2 extended in proto", proto)
protoa.append(proto2) # pass proto2 as an argument to the append method
print("proto2 appended to protoa", protoa)

# Challange 01 - Continue writing the script listmethods/listmeth02.py
# so that it demonstrates AT LEAST one of the methods found on
# https://docs.python.org/3/tutorial/datastructures.html

# remove the second item listed in proto2 of the fourth item listed in portoa
protoa[4].remove(proto2[1])
print("proto2's second item removed from protoa's fourth item", protoa)

# create another list of protocols, display it, reverse the elements in this list,
# replace the first element in protoa with protob, and display new portoa
protob = ["tcp/ip", "smtp", "ftp", "telnet", "arp", "snmp"]
print("protob:", protob)
protob.reverse()
protoa[0]=protob
print("new protoa:", protoa)
