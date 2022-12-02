##################################
# EECS1015 - York University
# Author: Michael S. Brown
# (c) MS Brown. This code cannot be shared without permission from the
# author.
# Lab 8 starter code
#
##################################
import random


def print_student_info():
    print("Name: MOHAMMAD IDRAK ISLAM")
    print("Student ID: 219284330")
    print("Section A or B")
    print("Email: idrak888@my.yorku.ca")


# class for task 2
class virus:
    def __init__(self, DNAinput=""):
        if DNAinput != "":
            if len(DNAinput) == 50:
                self.DNA = DNAinput
        else:
            new_DNA = ""
            for i in range(50):
                new_DNA += randomChar()

            self.DNA = new_DNA

    def getDNA(self):
        return self.DNA

    def replicate(self):
        randomNum = random.randint(1, 100)
        if randomNum > 94:
            randomIndex = random.randint(0, 49)
            mutatedDNA = self.DNA[:randomIndex] + randomChar() + self.DNA[randomIndex + 1:]
            x = virus(mutatedDNA)
        else:
            x = virus(self.DNA)

        return x


def randomChar():
    randomNum = random.randint(1, 4)
    if randomNum == 1:
        return "A"
    elif randomNum == 2:
        return "G"
    elif randomNum == 3:
        return "T"
    elif randomNum == 4:
        return "C"


def find_mutation(virus1, virus2):
    DNA1 = virus1.getDNA()
    DNA2 = virus2.getDNA()
    marker = ""

    for i in range(len(DNA1)):
        if DNA1[i] != DNA2[i]:
            marker += "^"
        else:
            marker += " "

    return marker


# class for task 1
class lotto_ticket:
    ticket_counter = 0

    def __init__(self):
        self.ticket_id = lotto_ticket.ticket_counter
        lotto_ticket.ticket_counter += 1

        numList = []
        counter = 0
        while counter < 5:
            newNum = random.randint(1, 20)
            if not (newNum in numList):
                numList.append(newNum)
                counter += 1

        self.numbers = set(numList)

    def print_ticket(self):
        print_text = ""

        for i in self.numbers:
            print_text += f"  {str(i):4}  "

        print(f"#[{self.ticket_id:3d}] {print_text}")

    def print_and_return_win(self, lotto_numbers):
        matches = 0
        win_amount = 0
        tickets_string = ""

        for i in lotto_numbers:
            if int(i) in self.numbers:
                matches += 1
                tickets_string += f" {'*' + str(i) + '*':4} "
            else:
                tickets_string += f" {str(i):4} "

        if matches == 3:
            win_amount = 2
        elif matches == 4:
            win_amount = 20
        elif matches == 5:
            win_amount = 100

        print(f"Ticket #[ {self.ticket_id}] {tickets_string} [{matches} matches, ${win_amount}]")
        return int(win_amount)


def lotto_draw():
    numList = []
    counter = 0
    while counter < 5:
        newNum = random.randint(1, 20)
        if not (newNum in numList):
            numList.append(newNum)
            counter += 1

    return set(numList)


def task0():
    print_student_info()


def task1():
    amount = 100
    print(f"You have ${amount}")

    running = True
    while running:
        num_tickets = int(input("How many lotto tickets do you want [$2 each]? "))

        if num_tickets * 2 > amount:
            continue
        elif num_tickets < 0:
            continue
        elif num_tickets == 0:
            running = False
            break
        else:
            amount -= 2 * num_tickets

        tickets = []
        for i in range(num_tickets):
            new_ticket = lotto_ticket()
            new_ticket.print_ticket()
            tickets.append(new_ticket)

        print("--LOTTO DRAW--")

        lotto_numbers = lotto_draw()
        num_string = ""
        for i in lotto_numbers:
            num_string += f"{i} "

        print(num_string)

        input("---Press enter to check your winnings---")
        for i in tickets:
            amount += i.print_and_return_win(lotto_numbers)

        print(f"You have ${amount}")

        if amount < 2:
            running = False
            break

    print(f"You have ${amount}")


def task2():
    running = True

    while running:
        name = input("Name of virus: ")
        my_virus = virus()
        original_virus = my_virus

        print(f"Original DNA sequence: {my_virus.getDNA()}")
        N = int(input("How many times to replicate? "))

        for i in range(0, N):
            my_virus = my_virus.replicate()
            print(f"Replica [ {i:4}] DNA sequence: {my_virus.getDNA()}")

        print(f"Comparing latest {name} virus to the original {name}.")
        print(original_virus.getDNA())
        print(my_virus.getDNA())

        markers = find_mutation(original_virus, my_virus)
        changes = markers.count("^")

        if changes == 0:
            print("No mutations detected.")
        elif changes < 5:
            print(markers)
            print(f"{changes} mutations -- virus is the same.")
        else:
            print(markers)
            print(f"{changes} mutations -- a *new* virus has been created")

        again = input("Try again? ").lower()
        if again == "n":
            running = False


def main():
    task0()
    print("\n--- Task 1: Lotto LESS Revisited ---")
    task1()
    print("\n--- Task 2: Virus mutator ---")
    task2()


if __name__ == "__main__":
    main()
