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

words = {"Colors": "red orange yellow green blue indigo violet white black brown".split(),
         "Shapes": "square triangle rectangle circle ellipse rhombus trapazoid chevron pentagon hexagon septagon octogon".split(),
         "Fruit": "apple orange lemon lime pear watermelon grape grapefruit cherry banana cantalope mango straberry tomato".split(),
         "Animals": "ant baboon badger bat bear beaver camel cat clam cougar coyote crew deer dog donkey duck eagle ferret fox frog goat goose hawk lion lizard llama mole monkey moose mouse mule newt otter owl panda parrot pigeon rabbit ram rat raven rhino salmon seal shark sheep skunk sloth snake spider stork swan tiger toad trout turkey turtle whale wolf wombat zebra".split()}


def displayBoard():
    print (HANGMANPICS[len(missedWords)])
    print("Category: " + category)
    print("missed: " + missedWords)
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

def getRandomCategory(dicts):
    #1.choose category
    #2. choosen category will choose words
    categories = list(words.keys())
    category = random.choice(categories)
    return category
    

def getRandomWord(words):
    word = random.choice(words)
    return word

   #category
   #key = random.choice(list(words.keys()))
   #print(random.choice(key))

missedWords = ""
correctWords = ""
gameIsDone = False
category = getRandomCategory(words)
listWords = words[category]
secretWord = getRandomWord(listWords)
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
