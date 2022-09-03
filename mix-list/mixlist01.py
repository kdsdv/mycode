#!/usr/bin/env python3

# create a list containing three items
my_list = [ "192.168.0.5", 5060, "UP" ]

# respectively display each item as they are in the list
print("The first item in the list (IP): " + my_list[0] )
print("The second item in the list (port): " + str(my_list[1]) )
print("The last item in the list (state): " + my_list[2] )

# create a list containing six items and display only the IP addresses
iplist = [ 5060, "80", 55, "10.0.0.1", "10.20.30.1", "ssh" ]
print("These are the only IP addresses in the iplist:", iplist[3], "and", iplist[4])
