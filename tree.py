print("    *")
print("   ***")
print("  *****")
print(" *******")
print("*********")


print ("1" + "1")
print ("1" * 5)

count = 1
times = 1
space = 4
while count <= 5:
    print (" " * space, "*" * times, sep = "")
    count = count + 1
    times = times + 2
    space = space - 1
