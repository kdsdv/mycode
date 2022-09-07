''' Python Basics
    Lab 49: requests library - Open APIs
    CUSTOMIZATION 01 | kdsdv '''

# CUSTOMIZATION 01: Retrieve the houses and books pertaining to the character

#!/usr/bin/python3
"""Alta3 Research - Exploring OpenAPIs with requests"""
# documentation for this API is at
# https://anapioficeandfire.com/Documentation

import requests

AOIF_CHAR = "https://www.anapioficeandfire.com/api/characters/"

# returns the information from the url
def getInformation(website):
    information = []

    for url in website:
        gotresp = requests.get(url)
        information.append(gotresp.json().get('name'))

    return information

def main():
        ## Ask user for input
        got_charToLookup = input("Pick a number between 1 and 1000 to return info on a GoT character: ")

        ## Send HTTPS GET to the API of ICE and Fire character resource
        gotresp = requests.get(AOIF_CHAR + got_charToLookup)

        # retrieve the character, house(s), and book(s)
        character = gotresp.json().get('name')
        houses = getInformation(gotresp.json().get('allegiances'))
        books = getInformation(gotresp.json().get('books'))

        characterinfo = f'\n{character} belongs to the following house(s) and appears in the following book(s):'
        print(f'{characterinfo}\n\tHouse(s):')  # display message to screen

        # displays 'None' if houses list is empty, otherwise displays the houses
        if houses == []:
            print('\t\tNone')
        else:
            for house in houses:
                print(f'\t\t{"".join(house)}')
        
        print(f'\n\tBook(s):')
        # displays 'None' books list is empty, otherwise displays the books
        if books == []:
            print(f'\t\tNone')
        else:
            for book in books:
                print(f'\t\t{"".join(book)}')

if __name__ == "__main__":
        main()
