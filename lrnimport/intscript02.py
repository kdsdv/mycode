''' Python Basics
    Lab 42: Scripting Commands with Python
    AUGMENT SCRIPT | kdsdv '''

#!/usr/bin/env python3
import subprocess  ## <-------- changed
import crayons  # access crayons

print('LAB 42  WALKTHROUGH', end='')
subprocess.call(["ip", "link", "show", "up"])
print("This program will check your interfaces.")
interface = input("Enter an interface, like, ens3: ")
subprocess.call(["ip", "addr", "show", "dev", interface])  ## <--- changed
subprocess.call(["ip", "route", "show", "dev", interface]) ## <--- changed

print('\nAUGMENT SCRIPT\nExploring subprocess module\'s check_output')  # displays message to screen  
echooutput = subprocess.check_output(['echo', 'Monty Python!'])  # runs echo cmd and gets it output
diroutput = subprocess.check_output('dir')  # runs dir cmd and gets it output
lsoutput = subprocess.check_output(['ls', '-l'])  # runs ls cmd and gets its output
# displays cmd outputs to screen, respectively
print(f"{crayons.magenta('echo output:')} {echooutput}")
print(f"{crayons.magenta('dir output:')} {diroutput}")
print(f"{crayons.magenta('ls output:')} {lsoutput}")
