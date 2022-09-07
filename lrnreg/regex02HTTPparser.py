''' Python Basics
    Lab 50: Searching with Regular Expressions
    CUSTOMIZATION 01 & 02 |  kdsdv '''

#!/usr/bin/env python3
"""Alta3 Research | RZFeeser
A script to demonstrate the power of Regular Expression (regex) and
the requests library."""

# standard library imports go above 3rd party imports (best practice)
import re

# python3 -m pip install requests
import requests

def main():
    """Search a website's content"""

    url = ""  # empty string
    matchcounter = 0  # counts the number of matches on a page

    # CUSTOMIZATION 01: Continue to run program until users enters 'q' or 'Q' to quit
    while url.lower() != 'q':
        print("\nWhere should we search?")
        url = input("> ")  # collect user input

        if url.lower() == 'q':
            break

        try:
            print(f"\nGreat! So we'll try to open this URL {url} to search for the phrase:")
            searchFor = input("> ")
            if searchFor.lower() == 'q':
                break

            try:
                resp = requests.get(url)  # Send HTTP GET
                searchMe = resp.text      # strip everything off the response as a string (text)
                
                # use the re.search() to determine if our website has the pattern we are looking for
                # it works by taking arguments, the first is the regex search pattern, and the second
                # is the string to search within
                
                if re.search(searchFor, searchMe):
                    matchcounter += 1  # increases counter by 1; # CUSTOMIZATION 02: Number of matches on page
                    print("Found a match!")
                else:
                    print("No match!")

                print(f'\nFound {matchcounter} matches')
            except:
                print(f'\nNot a vlid entry. Restarting...')
        except:
            print(f'\nNot a vlid entry. Restarting...')

if __name__ == "__main__":
    main()
