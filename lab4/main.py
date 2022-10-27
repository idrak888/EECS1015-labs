################################
# EECS1015 York University
# Lab 4 - Starter Code
# Name: Mohammad Idrak Islam
# Section A/B (A)
# Student id: 219284330
# Email: idrak888@my.yorku.ca
################################
import random
import time

num_of_jumps = 0


def print_student_info():
    print("Name: Mohammad Idrak Islam")
    print("Section A")
    print("Student id: 219284330")
    print("Email: idrak888@my.yorku.ca")


eye1 = '{o,o}'
eye2 = '{-,o}'
eye3 = '{o,-}'
body = '/)_) '
feet = ' " " '


def frame1(i):
    return f"  o   [  {i}]  \n /|\  \n / \  "


def frame2(i):
    return f" \o/  [  {i}]  \n  |   \n / \  "


# task 1 functions

def get_int_input(prompt, min_value, max_value):
    val = 0
    while val > max_value or val < min_value:
        val = int(input(prompt))

    return val


def get_yes(prompt):
    val = ""
    while val.lower() != "y" and val.lower() != "n":
        val = input(prompt).lower()

    if val == "y":
        return True
    else:
        return False


def draw_owl(position, randomize=False):
    space = " " * position

    if randomize:
        rnd = random.randint(1, 3)
        if rnd == 1:
            print(space + eye1)
        elif rnd == 2:
            print(space + eye2)
        else:
            print(space + eye3)
    else:
        print(space + eye1)

    print(space + body)
    print(space + feet)


def task1():
    N = get_int_input("How many times to move [2-20]?", 2, 20)
    T = get_int_input("How long to delay [1-1000ms]?", 1, 1000)
    rnd = get_yes("Randomize [Y/N]?")

    for i in range(0, N):
        draw_owl(i, rnd)
        time.sleep(T / 1000)


# task 2 functions

def get_float_input(prompt, min_value, max_value):
    val = -100
    while not (val <= max_value and val >= min_value):
        val = float(input(prompt))

    return val


def compute_return(amount, rate, years):
    amount_new = amount
    for i in range(years):
        x = amount_new + (amount_new * rate)
        amount_new = x
    return amount_new


def task2():
    run = True
    while (run):
        amount = get_float_input("Input initial investment amount [1, 10000]?", 1, 10000)
        rate = get_float_input("Annual return rate [0-1]?", 0, 1)
        years = get_int_input("How many years [1-10]?", 1, 10)

        if years > 1:
            print(f"Return in {years} years is: ${compute_return(amount, rate, years):.2f}")
        else:
            print(f"Return in {years} year is: ${compute_return(amount, rate, years):.2f}")

        run = get_yes("Compute new investment [Y/N]?")


def task3():
    global num_of_jumps
    largest = 1
    for i in range(0, 5):
        num = get_int_input(f"{i + 1}/5 Enter a number [1-100]:", 1, 100)
        if num > largest and num % 2 != 0:
            largest = num
    print(f"Final max odd number: {largest}")
    num_of_jumps = largest


def task4():
    input(f"Press enter to perform {num_of_jumps} jumping jacks")

    for i in range(num_of_jumps):
        if i % 2 == 0:
            print(frame1(i + 1))
        else:
            print(frame2(i + 1))
        time.sleep(0.3)


def main():
    print_student_info()

    print("\n---- Task 1: The Owl ----")
    task1()
    print("\n---- Task 2: Compound investment ---")
    task2()
    print("\n---- Task 3: Max odd number ----")
    task3()
    print("\n---- Task 4: Jumping Jacks ----")
    task4()
    input("Press enter to end lab 4.")


if __name__ == "__main__":
    main()
