######################################
# EECS1015 - Fall 2022
# Lab
#####################################
import random


def print_student_info():
    print("Name: Mohammad Idrak Islam")
    print("ID: 219284330")
    print("Section A")
    print("email: idrak888@my.yorku.ca")


def task0():
    print_student_info()

# Task 1

# Functions for task 1

def average_num(*nums):
    total = 0
    for i in nums:
        total += int(i.strip())
    return total / len(nums)


def task1():
    running = True
    while running:
        numOfNumbers = int(input("Input 4 or 5 numbers? "))

        if numOfNumbers == 4:
            numbers = input("Input 4 numbers [x1, x2, x3, x4]: ").split(",")
            x1, x2, x3, x4 = numbers
            print(f"Average is: {average_num(x1, x2, x3, x4)}")
        elif numOfNumbers == 5:
            numbers = input("Input 5 numbers [x1, x2, x3, x4, x5]: ").split(",")
            x1, x2, x3, x4, x5 = numbers
            print(f"Average is: {average_num(x1, x2, x3, x4, x5)}")

        again = input("Try again? ").lower()
        if again == "n":
            running = False


# Task 2

# Functions for task 2

def build_stock_dict(a_string):
    # "Apple:155.74:AAPL Tesla:228.52:TSLA Ford:13.26:F Microsoft:9.12:MSFT Shopify:34.19:SHOP"
    bigList = a_string.split(" ")
    stock_dict = {}
    for i in bigList:
        smallList = i.split(":")
        stock_dict[smallList[2]] = [smallList[0], float(smallList[1])]
    return stock_dict


def print_stock_dict(stock_dict):
    keys = list(stock_dict.keys())
    print("{:10s} {:6s}  {}".format("Symbol", "Price", "Company Name"))
    print("-" * 31)
    for k in keys:
        print(f"{k:7s} {stock_dict[k][1]:8.2f}   {stock_dict[k][0]}")
        # stock_dict[k][1]
        # ^^^^^^^^^^^^^    <- this gets the list for the key k
        #              ^^^ <- this retrieves item [1] in the list (price of stock)
        #
    print()  # <- an extra empty print to make it look nice


def task2():
    stock_dict1 = {"SNAP": ["Snap", 10.08], "PINS": ["Pinterest", 29.40], "GOOG": ["Google", 96.58]}
    stock_list_string = "Apple:155.74:AAPL Tesla:228.52:TSLA Ford:13.26:F Microsoft:9.12:MSFT Shopify:34.19:SHOP"
    print_stock_dict(stock_dict1)
    stock_dict2 = build_stock_dict(stock_list_string)
    print_stock_dict(stock_dict2)


# Task 3

# Functions for task 3

def create_rand_list():
    randList = []
    num_of_element = random.randint(5, 15)
    min_value = random.randint(5, 10)
    max_value = random.randint(20, 50)

    for i in range(0, num_of_element):
        randList.append(random.randint(min_value, max_value))

    return randList


def print_list(a_list):
    numString = ""

    print("---list---")

    if len(a_list) > 0:
        for i in a_list:
            numString += f"({i})->"
        numString += "(end)"
        print(numString)
    else:
        print("(empty)")


def delete_item_from_list(a_list, item):
    if not (item in a_list):
        return -1
    else:
        i = a_list.index(item)
        del a_list[i]
        return i


def task3():
    a_list = create_rand_list()
    running = True
    while running:
        print_list(a_list)
        delItem = int(input("Item to delete: "))
        result = delete_item_from_list(a_list, delItem)

        if result != -1:
            print(f"Item {delItem} successfully deleted at position {result}.")
        else:
            print(f"Item {delItem} could not be deleted.")

        again = input("Delete item [Y/N]?").lower()
        if again == "n":
            running = False


# Task 4

# Functions for task 4

def print_image(image):
    for i in image:
        print(i)


def uncompress_rle_image(rle_image):
    mainList = []
    for row in rle_image:
        charString = ""
        for col in row:
            charString += col[0] * col[1]
        mainList.append(charString)

    return mainList


def task4():
    rle_image1 = [[(5, '-')], [(2, ' '), (1, '|')], [(2, ' '), (1, '|')], [(1, ' '), (3, '-')]]
    rle_image2 = [[(9, ' '), (1, '.'), (1, '8'), (1, '.'), (1, ' ')], [(9, ' '), (3, '8'), (1, ' ')],
                  [(9, ' '), (3, '8'), (1, 'l')],
                  [(8, ' '), (1, 'j'), (4, '8'), (1, '.')], [(7, ' '), (1, '.'), (6, '8'), (1, '.')],
                  [(6, ' '), (1, '.'), (8, '8'), (1, '.')],
                  [(4, ' '), (1, '.'), (1, 'd'), (10, '8'), (1, 'b'), (1, '.'), (1, ' ')],
                  [(2, ' '), (1, '.'), (1, 'd'), (14, '8'), (1, 'b'), (1, '.')],
                  [(1, ' '), (1, '.'), (18, '8'), (1, 'b'), (1, '.')],
                  [(1, '.'), (21, '8')], [(22, '8')], [(3, '8'), (1, 'P'), (2, '"'), (1, '4'), (3, '8')],
                  [(1, '`'), (1, 'P'), (1, "'"), (5, ' '), (1, '.'), (4, ' '), (1, '.'), (5, ' '), (1, '`'), (1, 'q'),
                   (1, "'")],
                  [(1, ' '), (1, '`'), (1, '-'), (2, '.'), (4, '_'), (1, ':'), (2, ' '), (1, ':'), (4, '_'), (2, '.'),
                   (1, '-'),
                   (1, "'"), (1, ' ')], [(9, ' '), (1, ':'), (2, ' '), (1, ':')],
                  [(9, ' '), (1, ':'), (2, ' '), (1, ':')],
                  [(9, ' '), (1, ':'), (2, ' '), (1, ':')], [(9, ' '), (1, ':'), (2, ' '), (1, ':')],
                  [(9, ' '), (1, ':'), (2, ' '), (1, ':')],
                  [(7, ' '), (1, '\\'), (1, '('), (1, '/'), (1, '\\'), (1, ')'), (1, '\\'), (1, '/'), (1, ' '),
                   (1, 'm'), (1, 'h')]]
    rle_image3 = [[(52, '.')], [(52, '.')], [(25, '.'), (1, '/'), (1, '\\'), (25, '.')],
                  [(18, '.'), (6, '_'), (1, '/'), (2, '_'), (1, '\\'), (7, '_'), (17, '.')],
                  [(18, '.'), (2, '|'), (13, '-'), (2, '|'), (17, '.')],
                  [(18, '.'), (2, '|'), (13, ' '), (2, '|'), (17, '.')],
                  [(18, '.'), (2, '|'), (4, ' '), (1, '\\'), (3, '|'), (1, '/'), (4, ' '), (2, '|'), (17, '.')],
                  [(18, '.'), (2, '|'), (3, ' '), (1, '['), (1, ' '), (1, '@'), (1, '-'), (1, '@'), (1, ' '), (1, ']'),
                   (3, ' '), (2, '|'), (17, '.')],
                  [(18, '.'), (2, '|'), (4, ' '), (1, '('), (1, ' '), (1, '.'), (1, ' '), (1, ')'), (4, ' '), (2, '|'),
                   (7, '.'), (7, ' '), (3, '.')],
                  [(18, '.'), (2, '|'), (4, ' '), (1, '_'), (1, '('), (1, 'O'), (1, ')'), (1, '_'), (4, ' '), (2, '|'),
                   (7, '.'), (1, '|'), (1, 'E'), (1, 'X'), (1, 'I'), (1, 'T'), (1, ' '), (1, '|'), (3, '.')],
                  [(18, '.'), (2, '|'), (3, ' '), (1, '/'), (1, ' '), (1, '>'), (1, '='), (1, '<'), (1, ' '), (1, '\\'),
                   (3, ' '), (2, '|'), (7, '.'), (1, '|'), (2, '='), (2, '>'), (1, ' '), (1, '|'), (3, '.')],
                  [(18, '.'), (2, '|'), (2, '_'), (1, '/'), (1, '_'), (1, '|'), (1, '_'), (1, ':'), (1, '_'), (1, '|'),
                   (1, '_'), (1, '\\'), (2, '_'), (2, '|'), (17, '.')], [(18, '.'), (17, '-'), (17, '.')], [(52, '.')],
                  [(52, '.')]]

    print("\t\tImage 1\n")
    image1 = uncompress_rle_image(rle_image1)
    print_image(image1)
    print("\t\tImage 2\n")
    image2 = uncompress_rle_image(rle_image2)
    print_image(image2)
    print("\t\tImage 3\n")
    image3 = uncompress_rle_image(rle_image3)
    print_image(image3)


def main():
    task0()
    print("\n--- Task 1: Average numbers ---")
    task1()
    print("\n--- Task 2: Text to dictionary---")
    task2()
    print("\n--- Task 3: Deleting from list---")
    task3()
    print("\n--- Task 4: RLE decoding  ---")
    task4()

    input("Press enter to end lab 6.")


if __name__ == '__main__':
    main()
