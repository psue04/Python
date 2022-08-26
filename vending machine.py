#Vending machine

import math
import random

#initial money
print ("You have 5000")
initial= int(5000)

#items
item = {
    "yoghurt" : 1,
    "triangle gimbap" : 2,
    "cream pie" : 3,
    "ends shopping" : 4, 
    }


#choices
while True :
    choose = input()
    if choose == "1" :
        initial = initial - 1250
        print ("1250 deducted")
    elif choose == "2":
        initial = initial - 800
        print ("800 deducted")
    elif choose == "3":
        initial = initial -2500
        print ("2500 deducted")
    elif choose == "4":
        initial = initial - 0
        print ("End shopping")
        break

result = initial
print ("Your bank account: " + str(result))


