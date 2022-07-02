# weight = float(input("Enter your weight in kg: "))
# height = float(input("Enter your height in m: "))
#
# bmi = round((weight / height ** 2), 2)
# if bmi < 18.5:
#     print(f"your BMI is {bmi}, so you are under weight")
# elif bmi <= 25:
#     print(f"your BMI is {bmi}, so you have a normal weight")
# elif bmi <= 30:
#     print(f"your BMI is {bmi}, so you are overweight")
# elif bmi <= 35:
#     print(f"your BMI is {bmi}, so you are obese")
# else:
#     print(f"your BMI is {bmi}, so you are clinical obese")

# year = int(input("Which year do you want to check: "))
# check if it is divisible by 4
# if year % 4 == 0:
#     if year % 100 != 0 and year % 400 != 0:
#         print(f"so the year {year}, is a leap year")
#     # check if it is divisible by 4 and 400
#     elif year % 400 == 0:
#         print(f"so the year {year}, is a leap year")
#     # check if it is divisible by 4 and 100
#     elif year % 100 == 0:
#         print(f"so the year {year}, is a leap year")
# # so if it is not divisible by 4 or (100 and 400)
# else:
#     print(f"so the year {year}, is not a leap year")

# if year % 4 == 0 and year % 400 == 0 or year % 100 != 0:
#     print(f"so the year {year}, is a leap year")
# else:
#     print(f"so the year {year}, is not a leap year")
#
# if year % 4 == 0:
#     if year % 100 == 0:
#         if year % 400 == 0:
#             print("Leap year")
#         else:
#             print("not leap year")
#     else:
#         print("Leap year")
# else:
#     print("not leap year")

# if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
#     print(year, "is a leap year.")
# else:
#     print(year, "is not a leap year.")

# print("Welcome to the roller coaster")
# height = float(input("Enter your height in m: "))
#
# bill = 0
# if height >= 120:
#     print("you can ride the roller coaster")
#     age = int(input("What is your age: "))
#     if age < 12:
#         bill = 5
#         print("child ticket are $5")
#     elif age < 18:
#         bill = 7
#         print("teenager ticket are $7")
#     else:
#         bill = 12
#         print("Adult ticket are $12")
#
#     photo = input("Do you want a photo taken. Type 'y' for yes and 'n' for know: ").lower()
#
#     if photo == 'y':
#         bill += 3
#     print(f"your total ticket {bill}")
#
#     print("you are no eligible for the ride")

# print("Welcome to the python pizza deliveries")
# size = input("What size of pizza do you want S, M, or L: ").upper()
# add_pepperoni = input("Do you want pepperoni? Y or N: ").upper()
# extra_cheese = input("Do you want extra Cheese? Y or N: ").upper()

# price_size = 0
# pepperoni_price = 0
# cheese_price = 0
#
# if size == "S":
#     price_size = 15
#     if add_pepperoni == "Y":
#         pepperoni_price = 3
#     if extra_cheese == "Y":
#         cheese_price = 1
#     total_bill = pepperoni_price + price_size + cheese_price
#     print(f"Your total bill is ${total_bill}")
# elif size == "M":
#     price_size = 20
#     if add_pepperoni == "Y":
#         pepperoni_price = 3
#     if extra_cheese == "Y":
#         cheese_price = 1
#     total_bill = pepperoni_price + price_size + cheese_price
#     print(f"Your total bill is ${total_bill}")
# elif size == "L":
#     price_size = 25
#     if add_pepperoni == "Y":
#         pepperoni_price = 3
#     if extra_cheese == "Y":
#         cheese_price = 1
#     total_bill = pepperoni_price + price_size + cheese_price
#     print(f"Your total bill is ${total_bill}")

# bill = 0
#
# if size == "S":
#     bill += 15
# elif size == "M":
#     bill += 20
# else:
#     bill += 25
#
# if add_pepperoni == "Y":
#     if size == "S":
#         bill += 2
#     else:
#         bill += 3
#
# if extra_cheese == "Y":
#     bill += 1
# print(bill)

# print("Welcome to the roller coaster")
# height = float(input("Enter your height in m: "))
#
# bill = 0
# if height >= 120:
#     print("you can ride the roller coaster")
#     age = int(input("What is your age: "))
#     if age < 12:
#         bill = 5
#         print("child ticket are $5")
#     elif age < 18:
#         bill = 7
#         print("teenager ticket are $7")
#     elif age < 45:
#         bill = 12
#         print("Adult ticket are $12")
#     else:
#         bill = 0
#         print("Adult ticket are for more than age 45 is free")
#
#     photo = input("Do you want a photo taken. Type 'y' for yes and 'n' for know: ").lower()
#
#     if photo == 'y':
#         bill += 3
#         if age > 45:
#             bill = 0
#
#     print(f"your total ticket {bill}")
# else:
#     print("you are no eligible for the ride")

# print("Welcome to the love calculator")
# name1 = input("what is your name? \n")
# name2 = input("what is their name? \n")

# name = (name1 + name2).lower()
#
# true = name.count("t") + name.count("r") + name.count("u") + name.count("e")
# love = name.count("l") + name.count("o") + name.count("v") + name.count("e")
# true_love = true * 10 + love
#
# if true_love < 10 or true_love > 90:
#     print(f"your score is {true_love}%, you go together like coke and mentos")
# elif 40 <= true_love <= 50:
#     print(f"Your score is {true_love}%, you are okay together")
# else:
#     print(f"Your score is {true_love}%")

# OR

# combined_string = name1 + name2
# lower_case_string = combined_string.lower()
# t = lower_case_string.count("t")
# r = lower_case_string.count("r")
# u = lower_case_string.count("u")
# e = lower_case_string.count("e")
# true = t + r + u + e
#
# l = lower_case_string.count("l")
# o = lower_case_string.count("o")
# v = lower_case_string.count("v")
# e = lower_case_string.count("e")
# love = l + o + v + e
#
# love_score = int(str(true) + str(love))
#
# if (love_score < 10) or (love_score > 90):
#     print(f"your score is {love_score}%, you go together like coke and mentos")
# elif (love_score >= 40) and (love_score <= 50):
#     print(f"Your score is {love_score}%, you are okay together")
# else:
#     print(f"Your score is {love_score}%")

print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

# https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

# Write your code below this line 👇

print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
road = input("You are at the cross road. Where do you want to go ? Type left or right \n").lower()

if road == "left":
    lake = input('You\'ve come to a lake. There is an island in the middle of the lake. Type "wait" to wait for a '
                 'boat. Type "swim" to swim across \n').lower()
    if lake == "wait":
        house = input("You have arrived at the island unharmed. There is a house with three doors. one red, one blue, "
                      "one yellow which colour do you choose \n").lower()
        if house == "red":
            print("It's a room full of fire. Game over")
        elif house == "yellow":
            print("It's a safe room. You win")
        elif house == "yellow":
            print("It's a room full of water. You win")
        else:
            print("It's a room full of harem. Game over you pervert")
    else:
        print("Game over")
else:
    print("Game over")
