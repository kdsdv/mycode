''' Python Basics
    Lab 36: Read from files
    CUSTOMIZATION 03 & 04 | kdsdv '''

#!/usr/bin/env python3

filename = input('Which file needs to be loaded? ')  # CUSTOMIZATION 04: Prompt user for file
lineCounter = 0  # counts the number of lines in configlist

## create file object in "r"ead mode
#with open("vlanconfig.cfg", "r") as configfile:  # code for CUSTOMIZATION 03: vlanconfig.cfg was hard coded in file
with open(filename, "r") as configfile:  # code for CUSTOMIZATION 04: filename was retrieved from user
    ## readlines() creates a list by reading target
    ## file line by line
    configlist = configfile.readlines()

## file was just auto closed (no more indenting)

## each item of the list now has the "\n" characters back
print(f'\n{configlist}')

# Displays how many lines are in respective file listed under respective CUSTOMIZATION below
for line in configlist:
    lineCounter += 1
    line = line.strip('\n)')

#print(f'\n{lineCounter} lines are in vlanconfig.cfg')  # code for CUSTOMIZATION 03: vlanconfig.cfg was hard coded in file
print(f'\n{lineCounter} lines are in [filename]')  # code for CUSTOMIZATION 04: filename was retrieved from user


