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

import random, string, time

# Variables

italics = "\x1B[3m"
reset = "\x1B[23m"
name = ""
hp = 20

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
    global hp
    di = input("Which direction do you choose? Do you turn left? Do you turn right? Perhaps you walk straight. What if you stay? (l/r/f/s)\n")
    if 's' in di:
        # stay (almost always death because you're being followed)
        print("\n{}You stay in place, and the silence of the room fades into frightening dungeon noises. Water drips, rats skitter...{}".format(italics, reset))
        time.sleep(2)
        print("{}An angry, low rumbling sound is heard.{}".format(italics, reset))
        fight(0.7)
    elif 'l' in di:
        # left
        move(0.3)
    elif 'r' in di:
        # right
        move(0.3)
    elif 'f' in di:
        # forwards
        move(0.7)
    else:
        gameLoop() # recursive call to the loop to restart the decision process. There was an error parsing the input

def move(fightChance=0.3):
    win()
    exit(0)
    pass

def fight(difficulty=0.5):
    pass

def win():
    print("\n{}In the room ahead, you notice a dank looking chest in the center of the floor. You place your torch in a wall sconce, and open the chest. Inside it, you find a {}. After you pick up your prize, you look up, and the exit slowly appears in front of you, in the form of a stone block wall sliding out of the way. A well lit hallway leads to a stairwell, and at the top you exit out of a solid steel door.\n\nOutside that door, there are nothing but lush green fields of happiness forevermore...{}".format(italics, lostWords(3), reset))

def showLevel():
    pass

def randomWord():
    size = random.SystemRandom().choice([3,4,5,6,7,8])
    return ''.join(random.SystemRandom().choice(string.ascii_lowercase) for _ in range(size))

def lostWords(count=1):
    if count <= 1:
        # just a single word. No spaces needed
        return randomWord()
    else:
        sent = ""
        for word in range(0, count):
            if word == count-1:
                sent += randomWord()
            else:
                sent += randomWord() + " "
        return sent;

def cleanName(name):
    if len(name) == 0:
        name = randomWord()
    if len(name) > 1:
        fc = name[0].upper()
        rest = name[1:]
        name = fc + rest
    return name

# Game logic starts here

init()
gameLoop()
