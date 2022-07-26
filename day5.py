# # 🚨 Don't change the code below 👇
# student_heights = input("Input a list of student heights ").split()
# for n in range(0, len(student_heights)):
#     student_heights[n] = int(student_heights[n])
# # 🚨 Don't change the code above 👆
#
#
# # Write your code below this row 👇
# # find the sum of number using for loop
# student_height = 0
# for height in student_heights:
#     student_height += height
# # find the total number of students in the list
# student_number = 0
# for student in student_heights:
#     student_number += 1
# # find the average by dividing the total height by the number of student
# average = round(student_height / student_number)
# print(average)

# 🚨 Don't change the code below 👇
# 🚨 Don't change the code below 👇
#
# student_scores = input("Input a list of student scores ").split()
# for n in range(0, len(student_scores)):
#     student_scores[n] = int(student_scores[n])
# print(student_scores)
# # 🚨 Don't change the code above 👆
#
# # Write your code below this row 👇
# highest_score = 0
# for score in student_scores:
#     if score > highest_score:
#         highest_score = score
#         # print(highest_score)
#
# print(f"The highest score in the class is: {highest_score}")

# print any number divisible by 2
# 🚨 Don't change the code above 👆
# new_number = 0
# for i in range(1, 101):
#     if i % 2 == 0:
#         new_number += i
# print(new_number)
# # Or
# total = 0
# for number in range(2, 100, 2):
#     total += number
# print(total)
#
# for number in range(1, 101):
#     if number % 5 == 0 and number % 3 == 0:
#         print("FizzBuzz")
#     elif number % 3 == 0:
#         print("Fizz")
#     elif number % 5 == 0:
#         print("Buzz")
#     else:
#         print(number)

# Password Generator Project
import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

# Eazy Level - Order not randomised:
# e.g. 4 letter, 2 symbol, 2 number = JduE&!91
# a = ""
# for i in range(0, nr_letters):
#     random.shuffle(letters)
#     a += letters[i]
# b = ""
# for i in range(0, nr_symbols):
#     random.shuffle(symbols)
#     b += symbols[i]
# c = ""
# for i in range(0, nr_numbers):
#     random.shuffle(numbers)
#     c += numbers[i]
# easy_password = a + b + c
#
# print(f"Your password could be {easy_password}")

# Hard Level - Order of characters randomised:
# e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

# hard_password = list(easy_password)
# random.shuffle(hard_password)
# result = ''.join(hard_password)
# print(result)

# Angela Steps
# Eazy level
# password = ""
# for char in range(1, nr_letters + 1):
#     password += random.choice(letters)
# for char in range(1, nr_symbols + 1):
#     password += random.choice(symbols)
# for char in range(1, nr_numbers + 1):
#     password += random.choice(numbers)

# Hard level
password_list = []
for char in range(1, nr_letters + 1):
    password_list += random.choice(letters)
for char in range(1, nr_symbols + 1):
    password_list += random.choice(symbols)
for char in range(1, nr_numbers + 1):
    password_list += random.choice(numbers)
random.shuffle(password_list)
print(password_list)

password = ""
for char in password_list:
    password += char
