
#!/usr/bin/env python3
"""Alta3 Research || Author: RZFeeser@alta3.com"""

''' Python Basics
    Lab 38: Creating Functions
    CUSTOMIZATION 01, 02, & 03 | kdsdv '''

import crayons  # CUSTOMIZATION 01: access to crayons library
import yaml  # CUSTOMIZATION 03: access to pyyaml library

# CUSTOMIZATION 02: Function to connect to IP and then reboot it
def devicereboot(devicecmd):
    for ip in devicecmd.keys(): # loop through the dict
        print(f'Connectiong to... {crayons.green(ip)} ... {crayons.red("REBOOTING NOW!")}')

    return None

# function to push commands
def commandpush(devicecmd): # devicecmd==dict

    for ip in devicecmd.keys(): # looping through the dict
        # print(f'Handshaking. .. ... connecting with {ip}') # fstring
        print('Handshaking. .. ...', crayons.green(' connecting with'), '{}'.format(crayons.red(ip)))  # CUSTOMIZATION 01
        # we'll learn to write code that connects to devices here
        for mycmds in devicecmd[ip]:
            # print(f'Attempting to sending command --> {mycmds}')
            print(crayons.yellow("Attempting to sending command"), '--> {}'.format(crayons.cyan(mycmds)))  # CUSTOMIZATION 01
            # we'll learn to write code that sends cmds to device here

    return None

# start our main script
def main():
    """called at runtime"""

    # # dict containing IPs mapped to a list of physical interfaces and their state
    # devicecmd = {"10.1.0.1":["interface eth1/2", "no shutdown"], "10.2.0.1":
    # ["interface eth1/1", "shutdown"], "10.3.0.1":["interface eth1/5", "no shutdown"]}

    # CUSTOMIZATION 03: Reads a YAML file called 'devicecmd.yaml'
    with open('devicecmd.yaml') as fileIn:  # opens yaml file
        devicecmd = yaml.load(fileIn, Loader=yaml.FullLoader)  # loads the content from the yaml file

    print("Welcome to the network device command pusher") # welcome message

    ## get data set / CUSTOMIZATION 01
    print(crayons.blue("\nData set found\n")) # replace with function call that reads in data from file

    ## run
    commandpush(devicecmd) # call function to push commands to devices

    print()

    devicereboot(devicecmd) # CUSTOMIZATION 02: call function to connect to IP and then reboot it

# call our main function
main()
