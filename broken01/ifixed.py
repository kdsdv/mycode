#!/usr/bin/env python3
# A program that prompts a user for two operators and operation (plus or minus)
# the program then shows the result.
# The user may enter q to exit the program.
calc1 = 0.0
calc2 = 0.0
operation = ""

while (calc1 != "q"): # corrected SyntaxError by adding colon
    print("\nWhat is the first operator? Or, enter q to quit: ")
    calc1 = input() # corrected NameError by using the correction function name of input
    if calc1.upper() == "Q": # corrected by allowing lowercase input also
        break

    try:
        calc1 = float(calc1)

        print("\nWhat is the second operator? Or, enter q to quit: ")
        calc2 = input() # corrected NameError by using the correction function name of input
        if calc2.lower() == "q":
            break

        try:
            calc2 = float(calc2)

            print("\nEnter an operation to perform on the two operators (+ or -): ")
            operation = input() # corrected NameError by using the correction function name of input
            if operation == "+":
                print("\n" + str(calc1) + " + " + str(calc2) + " = " + str(calc1 + calc2))
                # corrected SyntaxError by enclosing new line with quotation marks
            elif operation == '-': # corrected SyntaxError by spelling the keyword correctly
                print("\n" + str(calc1) + " - " + str(calc2) + " = " + str(calc1 - calc2))
            else:
                print("\nNot a valid entry. Restarting...")
        except:
            print(f'\nNot a valid entry. Restarting...')
    except:
        print(f'\nNot a valid entry. Restarting...')

