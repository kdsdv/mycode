#!/usr/bin/env python3
"""Alta3 Research | RZFeeser
   if, elif, else - A simple program using conditionals to make a decision."""

try:
    message = 'The movie is about to begin, we recommend '
    
    # wrap connection in a float() to accept decimals as numbers
    connection = float(input("What is your connection speed in Mbps?"))

    # if input value was higher or equal to 25
    if connection >= 25:
        message = message + 'setting video to 4k.'
    elif connection >= 5:
        message = message + 'setting video to 1080p.'
    elif connection >= 2:
        message = message + 'setting video to 720p.'
    elif connection < 0:
        message = 'Connection speed is invalid.  Exciting the script.'
    else:
        message = message + 'finding another acces network.'

    print(message)

except:
    message = 'Connection speed is invalid.  Exiting the script.'
    print(message)
