#!/usr/bin/env python3
"""Python Basics
   Lab 28: Using while, if, elif, else
   Simple Guessing Game | kdsdv"""

def main():
    # A simple guessing program utilizing conditionals without a while True loop

    counter = 0  # initialize integer counter to 0
    answer = " " # initialize string answer to empty space

    # repeat until user's answer is correct
    while counter < 3 and answer != "Brian":
        counter += 1 # increase the counter

        # retrieve user's answer and allows for uppercase or lowercase answer
        answer = input('Finish the movie title, "Monty Python\'s The Life of ______": ')
        answer = answer.capitalize() # capitalizes the first character and converts remaining characters to lowercase

        # checks to see if user's answer is correct
        if answer  == "Brian": # user's answer matches
            print("Correct!")
        elif counter == 3: # three attempts have been made
            print("Sorry, the answer was Brian.")
        else: # answer is wrong and counter doesn't equal 3 
            print("Sorry, try again.")

main()
