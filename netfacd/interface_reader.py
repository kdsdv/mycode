''' Python Basics
    Lab 40: Exploring Network Interfaces
    CUSTOMIZATION 01 & 02  | kdsdv '''

#!/usr/bin/env python3

import netifaces  # access to netifaces

# CUSTOMIZATION 01: Returns just the IP address when passed an adapter name
def getIP(adapter):
    print(f'{adapter}\'s IP: {netifaces.ifaddresses(adapter)[netifaces.AF_INET][0]["addr"]}')

# CUSTOMIZATION 02: Returns just the MAC address when passed an adapter name
def getMAC(adapter):
    print(f'{adapter}\'s MAC: {netifaces.ifaddresses(adapter)[netifaces.AF_LINK][0]["addr"]}')

def main():
    print('LAB 40 WALKTHROUGH', end='')
    # print(netifaces.interfaces())  # returns a list of our interfaces

    for i in netifaces.interfaces():
        print('\n**************Details of Interface - ' + i + ' *********************')

        try:    # This is a new line, you also need to indent the code below this line by 4 whitespaces
            # print(netifaces.ifaddresses(i))  # returns the details of the interface; replaced with code below
            # returns a list that contains a dictionary with two values; replaced with code below
            #print(netifaces.ifaddresses(i)[netifaces.AF_LINK])
            print('MAC:', netifaces.ifaddresses(i)[netifaces.AF_LINK][0]['addr'])  # Prints the MAC address
            print('IP:', netifaces.ifaddresses(i)[netifaces.AF_INET][0]['addr'])  # Prints the IP address
        except:          # This is a new line
            print('Could not collect adapter information') # Print an error message
    
    print('\nCUSTOMIZATION 01: Returns just the IP address when passed an adapter name')
    for adapter in netifaces.interfaces():  # iterate through adapter list
        try:
            getIP(adapter)  # call getIP(adapter) function
        except:
            print('Could not collect adapter information') # Print an error message

    print('\nCUSTOMIZATION 02: Returns just the MAC  address when passed an adapter name')
    for adapter in netifaces.interfaces():  # iterate through adapter list
        try:
            getMAC(adapter)  # call getMAC(adapter) function
        except:
            print('Could not collect adapter information') # Print an error message

main()
