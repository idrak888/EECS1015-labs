#########
# EECS1015 Fall 2022
# Lab 3
# Name: Mohammad Idrak Islam
# Sudent id: 219284330
#########

print("---- Lab 3 ----")
print("Name: Idrak Islam")
print("Section A")
print("Student id: 219284330")
print("Email: idrak888@my.yorku.ca")

import random

# Task 1
print("\n---- Task 1: Simple order ----")

total = None
discount = None

print("**Select menu item**")
print(" (1) Coke  [$1.00]")
print(" (2) Dosa  [$2.50]")
print(" (3) Pizza [$2.25]")
print(" (4) Taco  [$1.50]")
print(" (5) Tea   [$1.00]")

selection = input("Selection: ")

if selection == "1":
    total = 1
elif selection == "2":
    total = 2.5
elif selection == "3":
    total = 2.25
elif selection == "4":
    total = 1.5
elif selection == "5":
    total = 1
else:
    print("Invalid selection - setting amount to $0")
    total = 0

print("**Discount**")
print(" (C) Child [under 18] (50% discount)")
print(" (A) Adult [18-64]")
print(" (S) Senior [65+] (25% discount)")

age = input("Selection age: ")

if age.lower() == "c":
    discount = 0.5
elif age.lower() == "a":
    discount = 0
elif age.lower() == "s":
    discount = 0.25
else:
    print(f"'{age}' is an invalid selection! Extra charge for you!")
    discount = -0.25

print(f"Amount   $  {total:.2f}")
print(f"Discount $  {total * discount:.2f}")
print("--------------------")
print(f"Total    $  {(1 - discount) * total:.2f}")

# Task 2
print("\n---- Task 2: Draw circle ----")

r = 100
while not (r >= 1 and r <= 10):
    r = int(input("Input size between 1-10: "))

for y in range(-10, 11):
    print("")
    for x in range(-10, 11):
        if (x**2) + (y**2) <= (r**2):
            print("*", end="")
        else:
            print(".", end="")


# task 3
print("\n---- Task 3: Dice pair expected value ----")

running = True

while running:
    total = 0
    N = int(input("Roll dice how many times? "))
    for i in range(0, N):
        die1 = random.randint(1, 6)
        die2 = random.randint(1, 6)
        print(f"[{die1}]  [{die2}] -- {die1 + die2:2d}  Roll {i + 1}")
        total += die1 + die2

    average = total / N
    print(f"Average dice pair value: {average:.2f}")
    again = input("Try again [Y/N]? ").lower()

    if again == "y":
        running = True
    else:
        running = False

# task 4
print("\n---- Task 4: Compute PI ----")

M = int(input("Input number of terms, M: "))

sum = 0
for n in range(0, M+1):
    numerator = (-1)**n
    denominator = (2*n) + 1
    sum += 4*(numerator/denominator)
    print(f"n={n} . . . adding fraction: {numerator}/{denominator}")
    print(f"our pi = {sum:.11f}")
    print(f"real pi = 3.14159265359")


# pause program until enter is pressed
print("\n---- Lab 3 Done ----")
input("Press enter to exit.")