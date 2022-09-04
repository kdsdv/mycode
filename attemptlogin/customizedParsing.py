#!/usr/bin/env python3
""" Python Basics
    Lab 34: Parsing Log Files
    CUSTOMIZATION 01 & 02 | kdsdv"""

# CUSTOMIZATION 01: Write code to match on the number of successful logins and display information to user
# CUSTOMIZATION 02: Write code that returns the IP address associated with the failed login
def main():
    lineNo = 0 # counts the number of lines in the file
    pattern = r'- - - - -] Authorization failed' # pattern to be searched
    failedLogins = 0 # counts the number of failed logins
    successfulLogins = 0 # counts the number of successful logins

    # read file searching for pattern and display the number of failed and successful logins to the screen
    with open('keystone.common.wsgi', 'r') as fileIn: # file being read
        for line in fileIn: # loops through each line in the file
            lineNo += 1 # increases counter by one
            #print(line, end='')
            if pattern in line: # checks to see if pattern appears in the line
                failedLogins +=1 # increases counter by one
                print('Failed login from ' + line.split(' ')[-1], end='') # displays IP address associated w/failed login
            else:
                successfulLogins += 1 # increases the counter by one

    print(f'\n{failedLogins} Failed Logins\n{successfulLogins} Successful Logins') # displays on the screen

main()

