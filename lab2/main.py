########################################
# EECS1015- Fall 2022
# Lab 2
#
# Your name: Mohammad Idrak Islam
# Your section: A
# Your student ID: 219284330
# Your email contact: playbox8g@gmail.com
#######################################

# Please fill out your info for each lab
print("---- Lab 2 ----")
print("Name: Idrak Islam")
print("Section A")
print("Student id: 219284330 ")
print("Email: playbox8g@gmail.com")

# Task 1
print("\n---- Task 1: Three year investment return ----")

name = input("Name: ").strip().title()
initial = float(input("Initial amount $: ").strip())
rate = float(input("Rate of return: %: ").strip())

y1 = initial + (initial * (rate / 100))
y2 = y1 + (y1 * (rate / 100))
y3 = y2 + (y2 * (rate / 100))

print(f"Client: {name}, year rate of return multiplier: {rate / 100}")
print(f"Year 1      Starting Amount: $ {initial:.2f}      Ending Amount: $ {y1:.2f}")
print(f"Year 2      Starting Amount: $ {y1:.2f}      Ending Amount: $ {y2:.2f}")
print(f"Year 3      Starting Amount: $ {y2:.2f}      Ending Amount: $ {y3:.2f}")

# Task 2
print("\n----Task 2 Leetspeak converter ----")

string = input("Type in a long string: ").strip().upper()
leetString = string.replace("T", "7").replace("A", "^").replace("E", "3").replace("I", "!").replace("B", "8")
leetString = leetString.replace("O", ".").replace("C", "<").replace("S", "$")

print(leetString)

# task 3
print("\n---- Task 3: Substring highlighter ----")

sentence = input("Type a sentence at the prompt below: \n>")
substr = input("Enter substring below to highlight: \n>")
highlighted = f"{sentence[0:sentence.find(substr)]}*{substr.upper()}*{sentence[sentence.find(substr) + len(substr):]}"

print(f"Sentence has {len(sentence)} characters, substring has {len(substr)} characters.")
print(f"Substring highlighted: \n> {highlighted}")

# task 4
print("\n---- Task 4: Exponent ----")

userIn = input("Input exponent in the form x^y: ")
base = userIn[0:userIn.find("^")]
exponent = userIn[userIn.find("^") + 1:]

print(f"Extracted numbers {base} {exponent}")
print(f"{base}^{exponent} = {int(base) ** int(exponent)}")

# pause program until enter is pressed
print("\n---- Lab 2 Done ----")
input("Press enter to exit.")