# Author: Ivan Perez
# Date: 9/24/17
# Description:
# Program takes input from a user to help identify objects in the sky.
# Not really based on much 'reality' so feel free to pull and make changes
# as you see best fit based on actual science.

def main():
    print("Hello, I will help you identify objects in the sky.")
    print("Please respond to each question with a 'yes' or 'no'.")
    size = input("Is it big? ")
    if size == 'yes':
        eyesBurning = input("Are your retinas burning? ")
        if eyesBurning == 'yes':
            print("It's the sun.")
        else:
            print("It's the moon.")
    elif size == 'no':
        moving = input("Is it moving? ")
        if moving == 'yes':
            velocity = input("So quickly that you'd almost miss it? ")
            if velocity == 'yes':
                howBright = input("Is it super bright? ")
                if howBright == 'yes':
                    explosion = input("Ending with a dramatic explosion? ")
                    if explosion == 'yes':
                        print("It's a Bolide. Look it up.")
                    else:
                        print("It's a fireball.")
                else:
                    print("It's a Meteor.")
            elif velocity == 'no':
                blinking = input("Is anything blinking? ")
                if blinking == 'yes':
                    print("It's a Airplane.")
                elif blinking == 'no':
                    astronauts = input ("Are astronauts waving at you? ")
                    if astronauts == 'yes':
                        print("It's the International Space Station.")
                    else:
                        print("It's an Artificial Satellite.")
        elif moving == 'no':
            twinkling = input("Is it twinkling? ")
            if twinkling == 'yes':
                print("It's a Star.")
            else:
                fuzzy = input("Is it kind of fuzzy with a tail? ")
                if fuzzy == 'yes':
                    print("It's a Comet.")
                else:
                    boat = input("Is it attached to a boat? ")
                    if boat == 'yes':
                        print("It's a Masthead Light.")
                    else:
                        print("It's a Planet.")

main()
