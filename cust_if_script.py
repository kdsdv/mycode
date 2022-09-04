#1/usr/bin/env python3
""" Python Basics
    Lab 27: Writing your own if-logic script
    Custom if-elif-else Script | kdsdv"""

def main():
    # A program that returns new Busch Gardens rides that children can enjoy based on height requirements
    print("What new Busch Gardens rides can my child enjoy based on height requirements?")
    
    try:
        height = float(input("How tall is your child in inches? ")) # retrieve child's height

        # check to see which height is matches the child's height and return the new rides, if applicable
        if height >= 54:
            rides = ["Alpengeist", "Tempesto"]
        elif height >= 52 and height <= 53.9:
            rides = ["Apollo's Chariot"] 
        elif height >= 48 and height <= 51.9:
            rides = ["Le Catapult", "Mach Tower", "Turkish Delight", "Der Autobahn", "Loch Ness Monster",
                    "Trade Wind", "Verbolten", "Finnegan's Flyer"]
        elif height >= 46 and height <= 47.9:
            rides = ["InvadR"+u"\u2122", "Le Scoot"]
        elif height >= 42 and height <= 45.9:
            rides = ["Escape from Pompeii"+u"\u00AE", "Kinder Karussel", "Roman Rapids"+u"\u00AE", "The Battering Ram",
                    "The Flying Machine"]
        elif height >= 40 and height <= 41.9:
            rides = ["Der Wirbelwind"]
        elif height >= 38 and height <= 39.9:
            rides = ["There are no new rides for this height."]
        elif height >= 36 and height <= 37.9:
            rides = ["There are no new rides for this height."]
        elif height >= 0 and height <= 35.9:
            rides = ["Height requirement not met for any rides."]
        else:
            print("\nHeight is invalid. Exiting the script.") # exit program if height is invalid
            return

        # Message stating where height requirements were retrieved from and when
        message = "\n\nNOTE: Height requirments for new rides retrieved on 08/02/2022 from Busch Gardens Williamsburg's website.\n"
        message = message + "Visit their website for additional height requirements:\n"
        message = message + "https://buschgardens.com/williamsburg/help/child-height-check-stations"

        print ("\n" + "\n".join(rides) + message) # display message

    except:
        print("\nHeight is invalid. Exiting the script.") # exit program if height is invalid

main()
