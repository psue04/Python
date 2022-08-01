#Simple number game
import random

guesses = 0
print ("Hello what is your name?")
myName = input()

number = random.randint(1, 20)
print ("Welcome" + myName + ". Let's play a game. I am thinking of a number between 1 to 20. You only have 6 chances")

while guesses < 6:
    print ("Take your guess")
    guess = input ()
    guess = int(guess)

    guesses = guesses + 1

    if guesses < number:
        print ("Your answer is too low")
    if guesses > number:
        print ("Your answer is too high")
    if guesses == number:
        break
    if guess == number:
        guesses = str(guesses)
print ("Good job" + myName + "You guessed the answer in " + guesses + "guesses!")

if guess != number:
    number = str(number)
print ("No. The number I was thinking of is " + number)