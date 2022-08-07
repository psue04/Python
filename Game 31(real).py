import random

def inputNumbers(number):
    while True:
        numbers = input("ME : ").split()
        if len(numbers) < 1 or 3 < len(numbers):
            continue
        if number + 1 != int(numbers[0]):
            continue

        correctNumbers = []
        for i in range(len(numbers)):
            correctNumbers.append(str(number + 1 + i))

        if correctNumbers == numbers:
            return numbers

number = 0
while number < 31:
    print("PC : ", end="")
    count = random.randint(1,3)
    for i in range(count):
        number += 1
        print(str(number) + " ", end="")
        if number > 31:
            break

        if number >= 31:
            break

    print()
    numbers = inputNumbers(number)

    number = int(numbers.pop())
