#math solving quiz
import math
from random import random

print ("Solve the math question")

#randoms
random1 = random.randint(1, 10)
random2 = random.randint(1, 10)
op = random.randint(1, 6)

if op == 1 :
    result = random1 + random2
    op = "+"
elif op == 2 :
    result = random1 - random2
    op = "-"
elif op == 3:
    result = random1 * random2
    op = "*"
elif op == 4:
    result = random1 / random2
    op = "/"
elif op == 5:
    result = random1 % random2
    op = "%"
elif op == 6:
    result = random1 ** random2
    op = "**"
    

#Correct or Wrong
print ("Type your answer")
print (random1, "*", random2, "=:"
answer = int(input())

while answer != result:
    print ("Wrong")
    if answer == result:
        print ("Correct")
        break
