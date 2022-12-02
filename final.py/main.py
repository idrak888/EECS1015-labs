###########################################
# EECS1015 - Practice Final Exam
# Fall 2022, York University
# Starting code
#
###########################################
import random


def student_info():
    print("Name: MOHAMMAD IDRAK ISLAM")
    print("Student ID: 219284330")
    print("Email: idrak888@my.yorku.ca")
    print("Section: A")
    print("Lab: 9 (final)")


def task0():
    student_info()


def task1():
    running = True

    while running:
        long_sentence = input("Type in a long sentence: ").split()
        substr = input("Remove words containing: ")
        with_substr = ""
        without_substr = ""

        for word in long_sentence:
            if word.find(substr) != -1:
                with_substr += word + " "
            else:
                without_substr += word + " "

        print(f"With substring: {with_substr.strip()}")
        print(f"W/O substring: {without_substr.strip()}")

        again = input("Try again? [Y/N]").lower()
        if again == "n":
            running = False


# write randomlist and reshape for task2 below

def randomlist(N):
    list = []

    for i in range(N):
        list.append(random.randint(0, 9))

    return list


def reshape(a_list, num_rows, num_cols):
    final_list = []

    for row in range(0, num_rows):
        col_arr = []
        for i in range(len(final_list) * num_cols, (len(final_list) * num_cols) + num_cols):
            col_arr.append(a_list[i])

        final_list.append(col_arr)

    return final_list


def task2():
    running = True
    while running:
        N = int(input("List length: "))
        a_list = randomlist(N)
        print(a_list)
        num_rows = 0
        num_cols = 0

        while num_rows * num_cols != N:
            num_rows = int(input("Rows: "))
            num_cols = int(input("Cols: "))
            if num_rows * num_cols == N:
                print(reshape(a_list, num_rows, num_cols))
            else:
                print(f"Error: {num_rows}*{num_cols} != {N}")

        again = input("Try again? [Y/N]").lower()
        if again == "n":
            running = False


# write function find_duplicates() for task 3 below

def find_duplicates(a_dict):
    keys = list(a_dict.keys())
    values = list(a_dict.values())
    duplicates = {}

    for i in range(len(keys)):
        for z in range(len(keys)):
            if values[i] == values[z] and i != z:
                if duplicates.get(values[i]) is None:
                    duplicates[values[i]] = [keys[i]]
                else:
                    duplicates.get(values[i]).append(keys[i])

    print(duplicates)


def task3():
    print("Input words, press enter to end.")
    counter = 1
    entry = True
    a_dict = {}

    while entry:
        word = input(f"[Input {counter:2}] Word: ").strip()
        if word == "":
            entry = False
        else:
            a_dict[counter] = word
            counter += 1

    print("Dictionary")
    print(a_dict)

    find_duplicates(a_dict)


# write class rangeChecker for task4 below

class rangeChecker:
    range_counter = 1

    def __init__(self, name, min, max):
        assert max > min, f"Max ({max}) must be greater than min ({min})"
        self.id = rangeChecker.range_counter
        rangeChecker.range_counter += 1

        self.name = name
        self.min_value = min
        self.max_value = max

    def within_range(self, number):
        if self.min_value <= number <= self.max_value:
            return True
        else:
            return False

    def outside_range(self, number):
        if number < self.min_value or number > self.min_value:
            return True
        else:
            return False

    def print(self):
        print(f"rangeChecker [{self.id:2}] '{self.name:10}' - {self.min_value:8.2f} <= num <= {self.max_value:8.2f}")


def task4():
    running = True
    while running:
        rangeCheckers = []
        for i in range(0, 3):
            values = input(f"Range {i} Name, Min, Max: ")
            values_arr = values.split(",")
            rangeCheckers.append(rangeChecker(values_arr[0].strip(), float(values_arr[1].strip()), float(values_arr[2].strip())))

        list_of_num = input("Input list of numbers x1,x2,..,xn: ").split(", ")

        for checker in rangeCheckers:
            checker.print()
            for i in list_of_num:
                print(f"Inside range [{float(i):8.2f}]: {checker.within_range(float(i))}")

        for checker in rangeCheckers:
            checker.print()
            for i in list_of_num:
                print(f"Outside range [{float(i):8.2f}]: {checker.outside_range(float(i))}")

        again = input("Try again?").lower()
        if again == "n":
            running = False


def main():
    task0()
    print("--- Task 1 ---")
    # task1()
    print("\n--- Task 2 ---")
    # task2()
    print("\n--- Task 3 ---")
    # task3()
    print("\n--- Task 4 ---")
    task4()


if __name__ == "__main__":
    main()
