''' Python Basics
    Lab 37: Archive with zipfile
    CUSTOMIZATION 01 | kdsdv '''

#!/usr/bin/env python3

import zipfile

# CUSTOMIZATION 01: Program determines if a file is a zip file or not
def main():
    filename = input('What file do you want to examine? ')

    if zipfile.is_zipfile(filename):
        print(f'{filename} is a zip file')
    else:
        print(f'{filename} is not a zip file')

main()
