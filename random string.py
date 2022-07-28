#Finding a set of factors

#use for loop, %, make data return factors if there're no remainders
# numbers to divide: 1 - 12

#number = int(input())

#count = 1
#resultArray = []
#while count <= number:
    #if (number % count) == 0:
        #resultArray.append(count)
   # count = count + 1


#print(resultArray)

#for count in range (1, num + 1):
    #print (count)




#Random String Generator
#receives len of str, outputs random string = len, random is lower ascii
#use string_generator(len)
import random

print ("Please enter a number")
length = int(input())

def string_generator(length):
    count = 1
    val = ""
    while count <= length:
        ran = random.randint(97, 122)
        val = val + chr(ran)
            #print (count, ran, chr(ran)
        count = count + 1
    return val

randomStr = string_generator(length)
print (randomStr)

