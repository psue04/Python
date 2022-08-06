import random

HANGMANPICS = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']


words = "ant baboon badger bat bear beaver camel cat clam cougar coyote crew deer dog donkey duck eagle ferret fox frog goat goose hawk lion lizard llama mole monkey moose mouse mule newt otter owl panda parrot pigeon rabbit ram rat raven rhino salmon seal shark sheep skunk sloth snake spider stork swan tiger toad trout turkey turtle whale wolf wombat zebra".split()

def displayBoard():
    #print ("remained: ", len(HANGMANPICS) - len(missedWords))
    print (HANGMANPICS[len(missedWords)])
    print("missed: " + missedWords)
    #print("correct: " + correctWords)
    #correctly guessed words
    #loop guess and check if theres correct letters, if there is, change wrong to "_"
    #print ("secret: ")
    word = ""
    for char in secretWord:
        if char in correctWords:
            word = word + char
        else:
            word = word + "_"
    print ("secret: " + word + "(" + secretWord + ")")
        
def getGuess():
    #1. cannot be more than one 
    #2. has to be alphabet
    #3. a word that has already been written

    guess = ""
    while True:
        guess = input()
        if len(guess) != 1:
            print ("Only one character")
            continue
        if guess not in "abcdefghijklmnopqrstuvwxyz":
            print ("Alphabet only")
            continue
        if guess in missedWords or guess in correctWords:
            print ("You typed the word before")
            continue
        return guess

def win():
    for char in secretWord:
        if char in correctWords:
            return False
    return True

def getRandomWord(words):
   # index = random.randint(0, len(words) - 1)
   # return words[index]
    word = random.choice(words)
    return word

missedWords = ""
correctWords = ""
gameIsDone = False
secretWord = getRandomWord(words)
win = False

#move wrong to "missed", move right to "correct"

while True:
    displayBoard()
    guess = getGuess()
    if guess in secretWord:
        correctWords = correctWords + guess
    else:
        missedWords = missedWords + guess

    if win or len(HANGMANPICS) == len(missedWords):
        gameIsDone = True

    if gameIsDone:
        break

#end game
#gussed the correct word
#HANGMANPICS and missedwords have the same value

    
gameIsDone()
