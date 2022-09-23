########################################
# EECS1015- Fall 2022
# Lab 1
#
# Your name: Mohammad Idrak Islam
# Your section: A
# Your student ID: 219284330
# Your email contact: playbox8g@gmail.com
#######################################

# Please fill out your info for each lab
print("---- Lab 1 ----")
print("Name: Idrak Islam")
print("Section A")
print("Student id: 219284330 ")
print("Email: playbox8g@gmail.com")

# Task 1
print('\n---- Task 1: Currency converter ----')

CAD = float(input("Amount in Canadian dollars:"))

print("Amount in other currencies: ")
print("USD: " + str(CAD * 0.76))
print("EUR: " + str(CAD * 0.75))
print("NGN: " + str(CAD * 322.24))
print("CNY: " + str(CAD * 5.250))
print("INR: " + str(CAD * 97.14))

# Task 2
print('\n---- Task 2: String math ----')

print("Enter three strings: ")
str1 = input("Str1: ")
str2 = input("Str2: ")
str3 = input("Str3: ")

print("String concatenation: ")

print("str1 + str2 + str3 = " + str1 + str2 + str3)
print("str3 + str2 + str1 = " + str3 + str2 + str1)
print("str2 + str1 + str3 = " + str2 + str1 + str3)

num = int(input("Input an integer"))
print("String multiply: ")

print("num x str1 = " + str1*num)
print("num x str2+str3 = " + (str2+str3)*num)

# Task 3
print("\n---- Task 3: Math operators ----")

x = int(input("Input integer x: "))
y = int(input("Input integer y: "))

print("Integer math: ")

print("x / y = " + str((x / y)))
print("x // y = " + str((x // y)))
print("x % y = " + str((x % y)))
print("x** y = " + str((x ** y)))

x = float(input("Input float x: "))
y = float(input("Input float y: "))

print("x / y = " + str((x / y)))
print("x // y = " + str((x // y)))
print("x % y = " + str((x % y)))
print("x** y = " + str((x ** y)))

# Task 4
print('\n---- Task 4: Simple cylinder computation ----')

radius = float(input("Radius: "))
height = float(input("Height: "))
PI = 355/113

surfaceArea = str((2 * PI * radius * height) + (2 * PI * (radius ** 2)))
volume = str(PI * (radius ** 2) * height)

print("Cylinder surface area: " + surfaceArea)
print("Cylinder volume: " + volume)

## Adding the final "input" causes python to wait on the user to press enter
## before exiting the program.
print("\n---- FINISHED ----")
input("Press enter to end.")