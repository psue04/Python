import random
import time

delay = 1

def displayIntro() :
    print("Your are in a land full of dragons. In front of you,")
    print("you see two caves. In one cave, the dragon is friendly")
    print("and will share his treasure with you. The other dragon")
    print("is greedy and hungry, and will eat you on sight.")
    print()

def chooseCave() :
    cave = ''
    while cave != '1' and cave != '2' :
        print("Which cave will you go into? (1 or 2)")
        cave = input()
    caveNumber = cave
    return cave

def checkCave(chosenCave) :
    print("chosenCave: " + chosenCave)
    print("You approach the cave...")
    time.sleep(1)
    print("It is dark and spooky...")
    time.sleep(1)
    print("A large dragon jumps out in front of you! He opens his jaws and...")
    print()
    time.sleep(1)
    friendlyCave = random.randint(1, 2)

    if int(chosenCave) == friendlyCave :
        print("Gives you his treasure!")
    else :
        print("Gobbles you down in one bite!!")

def askPlayAgain() :
    # this function always returns either yes or no

    playAgain = ''
    while playAgain != 'yes' and playAgain != 'no' :
        print("Do you want to play again? (yes or no)")
        playAgain = input()

    return playAgain

    
caveNumber = ""
playAgain = "yes"

while playAgain == "yes" or playAgain == 'y' :
    print("You have chosen yes. Game begin...")
    displayIntro()
    caveNumber = chosenCave()
    checkCave(caveNumber)
    playAgain = askPlayAgain()
    time.sleep(1)

while playAgain == "no" or playAgain == 'n' :
    print("You have chosen no. Game Over...")
    break


            
