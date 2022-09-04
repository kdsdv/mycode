#!/usr/bin/env python3
"""Python Basics
   Lab 28: Using while, if, elif, else
   CHALLENGE 02 | kdsdv"""

def main():
    # A simple guessing program utilizing conditionals without a while True loop

    """CHALLANGE 02: If the user's answer is shrubbery,
    then print to the screen You gave the super secret answer!, and exit the program"""

    counter = 0  # initialize integer counter to 0
    answer = " " # initialize string answer to empty space

    # repeat until user's answer is correct
    while counter < 3 and (answer != "Brian" and answer != "Shrubbery"):
        counter += 1 # increase the counter

        # retrieve user's answer and allows for uppercase or lowercase answer
        answer = input('Finish the movie title, "Monty Python\'s The Life of ______": ')
        answer = answer.capitalize() # capitalizes the first character and converts remaining characters to lowercase

        # checks to see if user's answer is correct
        if answer  == "Brian": # user's answer matches
            print("Correct!")
        elif answer == "Shrubbery":
            print("You gave the super secret answer!")
        elif counter == 3: # three attempts have been made
            print("Sorry, the answer was Brian.")
        else: # answer is wrong and counter doesn't equal 3 
            print("Sorry, try again.")

main()

