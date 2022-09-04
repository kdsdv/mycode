''' Python Basics
    Lab 36: Read from files
    CUSTOMIZATION 01 & 02 | kdsdv '''

#!/usr/bin/env python3
######## EXPLORE READ ##########
## create file object in "r"ead mode
configfile = open("vlanconfig.cfg", "r")

## display file to the screen - .read()
print(configfile.read())

## close file
configfile.close()

######## EXPLORE READLINES ##########
## re-create file object to explore new method
configfile = open("vlanconfig.cfg", "r")

## make a list of file lines - .readlines()
configlist = configfile.readlines()
print(configlist)


## Iterate through configlist
print('CUSTOMIZATION 01')
for x in configlist:
    # CUSTOMIZATION 01 - "Extra" linefeed is not included when the for-loop display's the vaule of x
    print(x, end='')

print('CUSTOMIZATION 02')
for x in configlist:
    # CUSTOMIZATION 02 - "Extra" whitespace is removed around the commands
    print(x.strip())

## Always close your file
configfile.close()

