#!/usr/bin/python3

# 7hrl-2017
#
# A very quick Rouge Like. I'm starting about 4 hours into the 7HRL, and will have to stop before 6 hours in.
#
# Created by Jared Dunbar'

# haiku -

# mechanization
# it is what makes the world go
# watch it burn slowly

# Variables

italics = "\x1B[3m"
reset = "\x1B[23m"
name = ""
x = 0
y = 0
score = 0
hp = 20

# levels

# x - wall
# d - door (game logic will determine if it connects)
# e - possible enemy location. They don't move because easy. They do hurt you though if they are in the way.

bigroom = [
['x','x','d','x','x'],
['x','e','o','e','x'],
['d','o','e','o','d'],
['x','e','o','e','x'],
['x','x','d','x','x']
]

# Functions

def init():
    global name
    print("Welcome to the dungeon of Fallland\n")
    name = input("Please enter your name, traveler.\n\n")
    name = cleanName(name)
    print("\nHello, {}. You have ventured far. You may be very brave, but this is not like any other place. Danger lurks around every corner, and nobody ever escapes from these dungeons.\n".format(name))
    sure = input("Are you sure you want to continue? (y/N)\n")
    if not "y" in sure and not "Y" in sure:
        print("\n{}You turn around, and die instantly as you get stabbed in the neck by the narrator.{}\n".format(italics, reset))
        exit(0)
    print("\n{}You enter the dungeon through a massive door. It creaks rather loudly, and echos for a long time. After you enter, you let the door shut lightly, but it still slams sharply, despite your best efforts to be as silent as possible. You light your torch, and begin to walk forwards.{}\n".format(italics, reset))

def gameLoop():
    global x, y, score, hp


def win():
    print("\n{}In the room ahead, you notice a dank looking chest in the center of the floor. You place your torch in a wall sconce, and open the chest. Inside it, you find {}".format(italics, reset))

def showLevel():
    pass

def cleanName(name):
    if len(name) > 1:
        fc = name[0].upper()
        rest = name[1:]
        name = fc + rest
    return name

# Game logic starts here

init()
gameLoop()
win()
