#!/usr/bin/env python3
"""Python Basics
   Lab 28: Using while, if, elif, else
   Simple Guessing Game | kdsdv"""

def main():
    # A simple guessing program utilizing conditionals

    counter = 0 # initialize integer counter to 0

    # repeat until user's answer is correct
    while True:
        counter = counter + 1 # increase the counter

        # prompt the user for an answer
        print("Finish the movie title, Monty Python's The Life of ...")

        # retrieve user's answer and allows for uppercase or lowercase answer 
        answer = input("Your guess: ")
        answer = answer.capitalize() # capitalizes the first character and converts remaining characters to lowercase

        # checks to see if user's answer is correct
        if answer  == "Brian": # user's answer matches
            print("Correct!")
            break # escapes the while loop
        elif counter == 3: # three attempts have been made
            print("Sorry, the answer was Brian.")
            break
        else: # try again until answer is correct and counter doesn't equal 3 
            print("Sorry, try again.")

main()
