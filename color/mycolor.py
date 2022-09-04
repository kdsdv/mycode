''' Python Basics
    Lab 41: Defining Functions
    MY COLOR SCRIPT (mycolor.py) | kdsdv '''

#!/usr/bin/env python3

import crayons  # access crayons

def main():  # start main script
    print('MY COLOR SCRIPT (mycolor.py)')  # display title

    print(f"{crayons.cyan('kds')} {crayons.magenta('dv')}")  # display cyan and magenta text to screen

    crayons.disable()  # disables the crayon package

    print(f"{crayons.cyan('kds')} {crayons.magenta('dv')}")  # displays default colored text since crayons was disabled

    crayons.DISABLE_COLOR = False  # enable crayons package

    print(f"{crayons.green('kds')} {crayons.yellow('dv')}")  # displays green and yellow text since crayons was enabled

    print(crayons.green('kds', bold=True), crayons.yellow('dv', bold=True))  # displays bolded green and yellow text to screen
    
main()  # call main function
