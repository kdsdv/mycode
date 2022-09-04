#!/usr/bin/env python3  # calls Python 3.x

from subprocess import call  # access to call and check_output functions

call(["ip", "link", "show", "up"])  # calls the call function that returns the interfaces that are currently in an up state
print("This program will check your interfaces.")  # displays message
interface = input("Enter an interface, like, ens3: ")  # prompts user for an interface to look up
call(["ip", "addr", "show", "dev", interface])  # issue ip route sow dev based on user input
