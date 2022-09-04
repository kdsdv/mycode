#!/usr/bin/env python3
"""Python Basics
   Lab 25: Testing if conditionals
   Example 3 | kdsdv"""

def main():

    # create string hostname by prompting for user input
    hostname = input("What value should we set for hostname? ")

    # return user input in lowercase format and test to see if it is true
    if hostname.lower() == "mtg":
        print("The hostname was found to be mtg")

main()
