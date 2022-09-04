#!/usr/bin/env python3

"""Python Basics
   Lab 31: Looping with for 
   CHALLENGE 01 | kdsdv"""

def agricultureList(list):
    agriculture = ', '.join(list)
    return agriculture


def main():
    '''CHALLENGE 01: Create a for-loop that displays the farms's data structure'''
    farms = [{"name": "NE Farm", "agriculture": ["sheep", "cows", "pigs", "chickens", "llamas", "cats"]},
         {"name": "W Farm", "agriculture": ["pigs", "chickens", "llamas"]},
         {"name": "SE Farm", "agriculture": ["chickens", "carrots", "celery"]}]

    print(f'\033[4mFARM\033[0m\t\t\033[4mAGRICULTURE\033[0m') # print header

    # Retrieve and display the contents of farms' data structure
    for farm in farms:
        print('{:15} {}'.format(farm.get('name', 'Unknown Farm'), agricultureList(farm.get('agriculture'))))

main()
