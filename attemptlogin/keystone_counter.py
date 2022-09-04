#!/usr/bin/env python3
""" Python Basics
    Lab 34: Parsing Log Files
    Parsing Script | kdsdv"""

# parse keystone.common.wsgi and return number of failed login attempts
def main():
    pattern = r'- - - - -] Authorization failed' # pattern to be searched
    failedLogins = 0 # counts the number of failed login attempts
    lineNo = 0 # counts the number of lines in the file

    # read source file searching for pattern, writes results to another file, and displays results to screen
    with open('keystone.common.wsgi', 'r') as fileIn: # file being read
        with open('failedLogins.txt', 'w') as fileOut: # file written to
            for line in fileIn: # loops through each line in the file
                lineNo += 1 # increases counter by one
                if pattern in line: # checks to see if pattern appears in the line
                    failedLogins +=1 # increases counter by one
                    fileOut.write('Found "' + pattern + '" on Line ' + str(lineNo) + ':\n' + line + '\n') # writes to file
                    print(f'Found "{pattern}" on Line {lineNo}:\n{line}') # displays on screen
            fileOut.write(str(failedLogins) + ' Failed Login Attempts\n') # writes to file

    print(f'{failedLogins} Failed Login Attempts') # displays on screen

main()
