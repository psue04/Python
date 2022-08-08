#Math Game
#1. Game between me and computer
#2. Only numbers
#3. 31 is loser
#4. Players can use 1~3 numbers

import random
import time

delay = 1

GAMEOVER = ['''
┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼
███▀▀▀██┼███▀▀▀███┼███▀█▄█▀███┼██▀▀▀
██┼┼┼┼██┼██┼┼┼┼┼██┼██┼┼┼█┼┼┼██┼██┼┼┼
██┼┼┼▄▄▄┼██▄▄▄▄▄██┼██┼┼┼▀┼┼┼██┼██▀▀▀
██┼┼┼┼██┼██┼┼┼┼┼██┼██┼┼┼┼┼┼┼██┼██┼┼┼
███▄▄▄██┼██┼┼┼┼┼██┼██┼┼┼┼┼┼┼██┼██▄▄▄
┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼
███▀▀▀███┼▀███┼┼██▀┼██▀▀▀┼██▀▀▀▀██▄┼
██┼┼┼┼┼██┼┼┼██┼┼██┼┼██┼┼┼┼██┼┼┼┼┼██┼
██┼┼┼┼┼██┼┼┼██┼┼██┼┼██▀▀▀┼██▄▄▄▄▄▀▀┼
██┼┼┼┼┼██┼┼┼██┼┼█▀┼┼██┼┼┼┼██┼┼┼┼┼██┼
███▄▄▄███┼┼┼─▀█▀┼┼─┼██▄▄▄┼██┼┼┼┼┼██▄
┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼
┼┼┼┼┼┼┼┼██┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼██┼┼┼┼┼┼┼┼┼
┼┼┼┼┼┼████▄┼┼┼▄▄▄▄▄▄▄┼┼┼▄████┼┼┼┼┼┼┼
┼┼┼┼┼┼┼┼┼▀▀█▄█████████▄█▀▀┼┼┼┼┼┼┼┼┼┼
┼┼┼┼┼┼┼┼┼┼┼█████████████┼┼┼┼┼┼┼┼┼┼┼┼
┼┼┼┼┼┼┼┼┼┼┼██▀▀▀███▀▀▀██┼┼┼┼┼┼┼┼┼┼┼┼
┼┼┼┼┼┼┼┼┼┼┼██┼┼┼███┼┼┼██┼┼┼┼┼┼┼┼┼┼┼┼
┼┼┼┼┼┼┼┼┼┼┼█████▀▄▀█████┼┼┼┼┼┼┼┼┼┼┼┼
┼┼┼┼┼┼┼┼┼┼┼┼███████████┼┼┼┼┼┼┼┼┼┼┼┼┼
┼┼┼┼┼┼┼┼▄▄▄██┼┼█▀█▀█┼┼██▄▄▄┼┼┼┼┼┼┼┼┼
┼┼┼┼┼┼┼┼▀▀██┼┼┼┼┼┼┼┼┼┼┼██▀▀┼┼┼┼┼┼┼┼┼
┼┼┼┼┼┼┼┼┼┼▀▀┼┼┼┼┼┼┼┼┼┼┼▀▀┼┼┼┼┼┼┼┼┼┼┼
┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼
''']

WINNER = ['''
 __     ______  _    _  __          ______  _   _ 
 \ \   / / __ \| |  | | \ \        / / __ \| \ | |
  \ \_/ / |  | | |  | |  \ \  /\  / / |  | |  \| |
   \   /| |  | | |  | |   \ \/  \/ /| |  | | . ` |
    | | | |__| | |__| |    \  /\  / | |__| | |\  |
    |_|  \____/ \____/      \/  \/   \____/|_| \_|
''']

myName = input("Enter your name: ")
print()

objective = ["Small", "Crazy", "Delicious", "Sweaty", "Smelly", "Rotten", "Manly", "Muscular", "Disgusting"]
noun = ["Coffee", "Granny", "Monster", "Octopus", "Cat", "Teacher", "Doll", "Robot", "Disaster"]
randomOne = random.choice(objective)
randomTwo = random.choice(noun)
name = randomOne + " " + randomTwo

def displayIntro():
    print ("STARTING GAME...")
    time.sleep(1)
    print ("Loading...")
    print ()
    time.sleep(2)
    time.sleep(1)
    print ("Welcome " + myName + "...")
    time.sleep(1)
    print ("...")
displayIntro()

def randomName():
    time.sleep(1)
    print ("Your opponent is " + name)
    time.sleep(2)
    print ()
randomName()

def choosePlayer():
    print (name + " is letting you go first")
    time.sleep (1)
choosePlayer()
    

def displayPlayer():
    print()
    print ("GAME START")
    time.sleep(1)
    print (myName + " vs " + name)
displayPlayer()

def lose():
    print (GAMEOVER)
    exit(0)

def win():
    print(WINNER)
    exit(0)

def calculate():
    answer = answer.append(append)

#stores all answer inputs
answer = ""

def startGame():
    while True:
        if answer == 31:
            lose()
        else:
            print("It's " + myName + " 's turn")
            print("How many numbers do you wish to enter?")
            answer = int(input())
            print()
            if answer not in "1,2,3":
                print("Please enter 1~3 numbers")
                answer = (input("Enter 1~3 numbers: "))
                print()
                continue
            if answer in "abcdefghijklmnopqrstuvwxyz":
                print("Numbers only")
                answer = (input("Enter numbers: "))
                print()
                continue
            if answer in answer:
                print ("You typed this number before")
                answer = (input("Enter other numbers: "))
                print()
            else:
            #Computer's turn
                 print ("Computer's turn is: ")
                 print (calculate)
                 startGame()

startGame()
