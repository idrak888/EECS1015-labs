##################################
# EECS1015 - York University
# Author: Michael S. Brown
# (c) MS Brown. This code cannot be shared without permission from the
# author.
# Lab 7 starter code
#
##################################


def print_student_info():
    print("Name: MOHAMMAD IDRAK ISLAM")
    print("Student ID: 219284330")
    print("Section A or B")
    print("Email: idrak888@my.yorku.ca")


def task0():
    print_student_info()


def is_sorted(a_list):
    for i in range(len(a_list)):
        if i < len(a_list) - 1:
            if a_list[i + 1] < a_list[i]:
                return False
    return True


def task1():
    x1 = [1, 4, 5, 9, 0, 8, 10]
    x2 = [1, 2, 4, 5, 6, 7, 9]
    x3 = []
    # Write function is_sorted() outside this function
    # apply the function on each list and print the results
    print(is_sorted(x1))
    print(is_sorted(x2))
    print(is_sorted(x3))


def merge_dict(dict1, dict2):
    for i in dict2.keys():
        if not (i in dict1):
            dict1[i] = dict2[i]


def task2():
    dict1 = {8: "Exercise", 9: "Breakfast", 12: "Lunch", 3: "Study", 6: "Netflix"}
    dict2 = {8: "Sleep", 10: "Lab", 12: "Class", 4: "Call Mom"}
    # Write function merge_dict() outside this function
    print(f"dict1: \n{dict1}")
    print(f"dict2: \n{dict2}")
    merge_dict(dict1, dict2)
    print(f"dict2 merged into dict1: \n{dict1}")


def invert_dict(a_dict):
    inverted = {}
    keys = list(a_dict.keys())
    size = len(keys)
    values = []

    for i in a_dict:
        values.append(a_dict.get(i))

    for i in range(size):
        inverted[values[i]] = keys[i]

    return inverted


def task3():
    a_dict = {1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five'}
    print(a_dict)
    inverted = invert_dict(a_dict)
    print(inverted)


def list_to_dict(a_list):
    a_dict = {}
    for i in range(len(a_list)):
        a_dict[i] = a_list[i]
    print(a_dict)


def task4():
    my_list = [1, "hello", 9.99, ["EECS", "1015"], {1: "1", 2: "2"}]
    # write function list_to_dict() outside this function
    # print list
    # call list_to_dict(my_list)
    # print new dictionary
    list_to_dict(my_list)


def str_list_to_num_list(a_list):
    for i in range(len(a_list)):
        a_list[i] = int(a_list[i])


def task5():
    x = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    print(x)
    str_list_to_num_list(x)
    print(x)


def merge_lists(list1, list2):
    new_list = []
    len1 = len(list1)
    len2 = len(list2)
    index1 = 0
    index2 = 0

    assert is_sorted(list1), "List 1 is not sorted!"
    assert is_sorted(list2), "List 2 is not sorted!"

    while index1 < len1 and index2 < len2:
        if list1[index1] <= list2[index2]:
            new_list.append(list1[index1])
            index1 += 1
        else:
            new_list.append(list2[index2])
            index2 += 1
    if index1 < len1:
        new_list.extend(list1[index1:])
    if index2 < len2:
        new_list.extend(list2[index2:])
    return new_list


def task6():
    running = True
    while running:
        l1 = input("Input 1st sorted list of numbers [x1 x2 ...]: ").split()
        l2 = input("Input 2nd sorted list of numbers [x1 x2 ...]: ").split()
        str_list_to_num_list(l1)
        str_list_to_num_list(l2)

        print(merge_lists(l1, l2))

        again = input("Try again [Y/N]? ").lower()
        if again == "n":
            running = False


def main():
    print("\n---- Task 1: Check if list is sorted ----")
    task1()
    print("\n---- Task 2: Merge dictionaries ----")
    task2()
    print("\n---- Task 3: Invert dictionaries ----")
    task3()
    print("\n---- Task 4: List to dictionary ----")
    task4()
    print("\n---- Task 5: String list to num list ----")
    task5()
    print("\n---- Task 6: Merge list with assert ----")
    task6()


if __name__ == "__main__":
    main()
