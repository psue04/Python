#StringModifier

#Leave the last 3 letters of the entered student number and replace them with '*' characters.
#exp: 2022020789 =>********789

print ("Enter your student number: ")

studentID = input()
count = len(studentID) - 3
print("*" * count + studentID[7:])
