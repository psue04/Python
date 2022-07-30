#Max Number Finder

#find the maximum value in an array in which a random number is stored.
#Use the for statement to print the largest number in the list
#At this time, the index where the most number is located is output.

#List of random numbers

import random

list = [random.randrange(1, 100) for i in range(10)]
print(list)

#Find Max

maxNum = list[0]
index = 0
indexOfMaxNum = 0
for l in list:
    print (l)
    if maxNum < l:
        maxNum = l
        indexOfMaxNum = index
    index = index + 1

print ("maxNum: ", maxNum)
print ("indexOfMaxNumber: ", indexOfMaxNum)
