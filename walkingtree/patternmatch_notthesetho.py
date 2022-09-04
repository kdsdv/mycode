#Author: RZFeeser RZFeeser@alta3.com

''' Python Basics
    Lab 45: Walking the Directory Tree
    LAB STEP 23 & CUSTOMIZATION 01 & 02 | kdsdv '''

"""Script to search for a pattern match"""
#!/usr/bin/env python3

import os # used to walk the system
import fnmatch # for regex pattern matching

# CUSTOMIZATION 02: argparse accepts arguments at the command-line
import argparse  # used to parse arguments passed at the command-line

# create the parser, add the arguments, and parse the arguments
parser = argparse.ArgumentParser (description='Locate a Pattern in the Filesystem')
parser.add_argument('lookfor', type=str, help='What pattern am I looking for (Example: *.txt or *.cfg)?')
parser.add_argument('lookwhere', type=str, help='What is the path in which I should search?')
args = parser.parse_args()

# LAB STEP 23: added/removed other directories from the EXCLUDE list
EXCLUDE = ["/", "/home", "/static"] ## Don't search in these locations

# EXCLUDE = ["/usr", "/home", "/var"] ## Don't search in these location

def find(pattern, path):
    """search through filesystem based on given path location"""
    result = []
    for root, dirs, files in os.walk(path, topdown=True):
        if root in EXCLUDE: # if the root matches the exclude list
            dirs[:] = [] # remove the directory list for this iteration
            files[:] = [] # remove the file list for this iteration
        for name in files: # always perform the nested loop, but it maybe empty
            if fnmatch.fnmatch(name, pattern): # if match
                result.append(os.path.join(root, name)) # add to our list
    return result # return the list

def main():
    """runtime code"""

    # CODE for USER IINPUT (CUSTOMIZATION 01 is part of this code)
    #lookfor = input("What pattern am I looking for (Example: *.txt or *.cfg) ")
    #lookwhere = input("What is the path in which I should search? ")
    
    ## CUSTOMIZATION 01: Code insensitive to capitals: 'lookfor.lower()'
    #print("Results: ", find(lookfor.lower(), lookwhere)) # call function

    # CUSTOMIZATION 02: prints the results after the search is done
    print("Results: ", find(args.lookfor.lower(), args.lookwhere)) # call function

main()

