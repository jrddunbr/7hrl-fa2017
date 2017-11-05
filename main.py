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

import random, string, time, getch

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
    print("\n{}You walk forwards...{}".format(italics, reset))
    time.sleep(1)
    ia = random.random()
    if ia < 0.05:
        win()
    elif ia < fightChance:
        fight()
    else:
        print("{}... and nothing super bad happens. {}{}".format(italics, randomAction(), reset))
        gameLoop()
    exit(0)
    pass

def fight(difficulty=0.4):
    global hp
    print ("\n{}A fight breaks out!\n\nSuddenly, {}{}".format(italics, badThing(), reset))
    print("Press keys on your keyboard to ward off the enemy!")
    result = attack()
    hp = hp - result
    print("You loose {} hearts".format(int(result/2)))
    if hp < 0:
        print("\n{}You die in the attack.{}".format(italics, reset))
        exit(0)
    else:
        for heart in range(0, int(hp/2.0)):
            print(" ♥", end="")
        if hp%2 != 0:
            print(".")
        print("\n{}You live to tell the tale.{}".format(italics, reset))
        gameLoop()

def win():
    print("\n{}In the room ahead, you notice a dank looking chest in the center of the floor. You place your torch in a wall sconce, and open the chest. Inside it, you find a {}. After you pick up your prize, you look up, and the exit slowly appears in front of you, in the form of a stone block wall sliding out of the way. A well lit hallway leads to a stairwell, and at the top you exit out of a solid steel door.\n\nOutside that door, there are nothing but lush green fields of happiness forevermore...{}".format(italics, lostWords(3), reset))

def showLevel():
    pass

def randomAction():
    return "A rat skitters across the floor, causing you to jump."

def badThing():
    return "a hungry wolf leaps from the dark!"

def attack():
    start = time.time()
    keys = ""
    while len(keys) < 30:
        keys += str(getch.getch())
    stop = time.time()
    ti = stop-start
    if ti < 5:
        return 8
    elif ti < 3:
        return 6
    elif ti < 2:
        return 4
    elif ti < 1.5:
        return 2
    else:
        return 0

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
