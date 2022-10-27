################################
# EECS1015, York University
# Lab 5 starting code
# Name:  Mohammad Idrak Islam
# Section:  Section A
# Student ID: 219284330
# Email:  idrak888@my.yorku.ca
################################

import random


# Print info
def print_lab_info():
    print("---- Lab 5 ----")
    print("Name: Idrak Islam")
    print("Section A")
    print("Student id: 219284330")
    print("Email: idrak888@my.yorku.ca")


def task0():
    # Example of calling a function from taskX() functions.
    # you should write all functions "outside" your task1()-task4() functions.
    print_lab_info()


def input_list():
    intList = []
    val = 0
    while val >= 0:
        val = int(input("Input positive int: "))
        if val >= 0:
            intList.append(val)
        else:
            break
    return intList


def compute_average(intList):
    sum = 0
    for i in intList:
        sum = sum + i

    if len(intList) > 0:
        return sum / len(intList)
    else:
        return 0

def task1():
    running = True
    while running:
        avg = compute_average(input_list())
        print(f"List average {avg:.2f}")
        again = input("Do again? [Y/N] ").lower()

        if again == "n":
            running = False


def task2():
    longString = input("Input a long string: ").upper()
    strList = []

    for x in longString:
        strList.append(x)

    strSet = set(strList)
    strDict = {}

    for y in strSet:
        strDict[y] = 0

    for z in strList:
        strDict[z] = strDict[z] + 1

    for i in strDict:
        print(f"{i} | {'*'*strDict[i]}")


def task3():
    encoder = {'A': '$', 'B': 'F', 'C': 'C', 'D': '2', 'E': 'B', 'F': 'I', 'G': '=', 'H': '*', 'I': '"', 'J': ']',
               'K': '1',
               'L': '0', 'M': '@', 'N': '[', 'O': 'L', 'P': '%', 'Q': '&', 'R': '(', 'S': 'G', 'T': 'K', 'U': '5',
               'V': '!',
               'W': '^', 'X': '+', 'Y': '6', 'Z': '-', '1': 'H', '2': 'A', '3': 'J', '4': '7', '5': '4', '6': 'D',
               '7': 'E',
               '8': '9', '9': ')', '0': ';', ',': '3', '.': '/', ' ': '_'}
    decoder = {'$': 'A', 'F': 'B', 'C': 'C', '2': 'D', 'B': 'E', 'I': 'F', '=': 'G', '*': 'H', '"': 'I', ']': 'J',
               '1': 'K',
               '0': 'L', '@': 'M', '[': 'N', 'L': 'O', '%': 'P', '&': 'Q', '(': 'R', 'G': 'S', 'K': 'T', '5': 'U',
               '!': 'V',
               '^': 'W', '+': 'X', '6': 'Y', '-': 'Z', 'H': '1', 'A': '2', 'J': '3', '7': '4', '4': '5', 'D': '6',
               'E': '7',
               '9': '8', ')': '9', ';': '0', '3': ',', '/': '.', '_': ' '}

    running = True
    while running:
        msg = input("Input message: ").upper()
        op = input("Encode (E) or Decode (D)? ").lower()

        if op == "e":
            encodedStr = ""
            for i in msg:
                encodedStr = f"{encodedStr}{encoder[i]}"
            print(f"Encoded message: \n {encodedStr}")
        else:
            decodedStr = ""
            for i in msg:
                decodedStr = f"{decodedStr}{decoder[i]}"
            print(f"Decoded message: \n {decodedStr}")

        again = input("Encode/decode again [Y/N]? ").lower()
        if again == "n":
            running = False

def random_set():
    numList = []
    counter = 0
    while counter < 5:
        newNum = random.randint(1, 20)
        if not (newNum in numList):
            numList.append(newNum)
            counter += 1

    return set(numList)

def print_set(aSet, prompt=""):
    printText = prompt + " "

    for i in aSet:
        printText += str(i) + " "

    print(printText)


def task4():
    running = True
    while running:
        valid = False
        numSet = {}

        while not valid:
            numInput = input("Enter 5 numbers between 1-20:")
            numSet = set(numInput.split(" "))
            if len(numSet) == 5:
                inRange = True
                for i in numSet:
                    if int(i) < 1 or int(i) > 20:
                        inRange = False

                if inRange:
                    valid = True

        compSet = random_set()
        matches = 0
        matchedChars = ""
        print_set(compSet, "Computer's numbers: ")

        for i in numSet:
            if int(i) in compSet:
                matches += 1
                matchedChars += f"{str(i)} "

        print(f"{matches} matches found: {matchedChars}")

        again = input("Try again [Y/N]? ").lower()
        if again == "n":
            running = False


def main():
    ### Don't forget to update print_lab_info() function
    task0()

    print("\n---- Task 1: List average ----")
    task1()

    print("\n---- Task 2: Character count graph ----")
    task2()

    print("\n---- Task 3: Encoder/decoder ----")
    task3()

    print("\n---- Task 4: Lotto LESS ----")
    task4()


if __name__ == "__main__":
    main()