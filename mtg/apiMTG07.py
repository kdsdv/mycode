''' Python Basics
    Lab 48: RESTful APIs and JSON
    CUSTOMIZATION 01 | kdsdv '''

#!/usr/bin/env python3
"""Alta3 Research | Author: RZFeeser@alta3.com

   Description:
   A script to interact with an "open" api,
   https://api.magicthegathering.io/v1/

   documentation for the API is available via,
   https://docs.magicthegathering.io/"""

# imports always go at the top of your code
import requests

# Define our "base" API
API = "https://api.magicthegathering.io/v1/" # this will never change regardless of the lookup we perform

def main():
    """Run time code"""

    cardcounter = 0  # counts how many cards are in a cardset
    subtypecounter = 0  # counts how many subtypes theare are

    setcode = input("What is the code of the set you are trying to lookup (see mtgsets.index for a list of codes)? ").lower()   # collect user input for MTG card set to lookup

    # create resp, which is our request object
    resp = requests.get(f"{API}cards?set={setcode}")   # this "f" string reads: API + "cards/" + setcode

    # the .json() method will dump a JSON string into Pythonic data structures. COOL!
    # This is much easier than using the urllib.request library
    cardset = resp.json().get('cards')

    # CUSTOMIZATION 01: Write the card data retrieved from and api into a file, naming it with the
    # cardset's code that the user is trying to look up, and ensure that it is readable
    with open(f'{setcode}_cards.set', 'w') as fileOut:
        for card in cardset:
            cardcounter += 1  # increases by 1
            fileOut.write(str(card) + '\n')

    setmsg = f'\nCUSTOMIZATION 01\n{setcode}_cards.set has been created. There are {cardcounter} cards in this card set.'
    print(f'{setmsg}')

    # CUSTOMIZATION 02: Interact with 'subtypes' and write them to a file
    # create resp, which is our request object
    resp = requests.get(f"{API}subtypes")
    
    subtypes = resp.json().get('subtypes')  # get subtype's data

    # loop through subtypes, increase counter, and write the subtypes to a file
    with open('subtype.txt', 'w') as fileOut:
        for subtype in subtypes:
            subtypecounter += 1
            stype = subtype.strip().split(',')
            fileOut.write(str(stype) + '\n')

    subtypemsg = f'\nCUSTOMIZATION 02\nsubtype.txt has been created. There are {subtypecounter} subtypes.'
    print(f'{subtypemsg}')
        
if __name__ == "__main__":
    main()
