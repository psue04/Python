from random import random
import random
import re
from string import capwords

number = random.randint(1,9)
number2 = random.randint(1,9)

result = number * number2
print(str(number) + "x" + str(number2) + "=" )

print("Guess the answer!")
otherNumber = input()

while otherNumber != result:
    print
    if otherNumber < result:
        print ("The answer is too low!")
        otherNumber = int(input("Enter a higher number: "))
    elif otherNumber > result:
        print ("The answer is too high!")
        otherNumber = int(input("Enter a lower number: "))
    elif otherNumber == result:
        print ("Correct!")
        break
    print
    
