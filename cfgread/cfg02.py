''' Python Basics
    Lab 36: Read from files
    Following Steps 15-18 | kdsdv '''

##!/usr/bin/env python3
## create file object in "r"ead mode
configfile = open("vlanconfig.cfg", "r")

## display file to the screen - .read()
configblog = configfile.read()

## break configblog across line boundaries (strips out \n)
configlist = configblog.splitlines()

## display list with no "\n"
print(configlist)

## Always close your file
configfile.close()

