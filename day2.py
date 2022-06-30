# # two_digit_number = input("Type any two digit number: ")
# # new_two_digit_number = str(two_digit_number)
# # first_digit = int(new_two_digit_number[0])
# # second_digit = int(new_two_digit_number[1])
# # print(first_digit + second_digit)
#
# # print(3 / 3 * 3 + 3 - 3)
#
# weight = input("Enter your weight in kg: ")
# height = input("Enter your height in m: ")
#
# new_weight = float(weight)
# new_height = float(height) ** 2
#
# bmi = int(new_weight / new_height)
# new_bmi = str(bmi)
# print("your bmi is " + new_bmi)

# Your life in a week
# age = input("what is your current age ? ")
# age_as_int = int(age)
# remaining_years = 90 - age_as_int
# remaining_months = remaining_years * 12
# remaining_weeks = round(remaining_years * 52)
# remaining_days = round(remaining_years * 365)
# print(f"You have {remaining_days} days, {remaining_weeks} weeks, {remaining_months} months left")

print("Welcome to the tip calculator \n")
bill = float(input("What was the total bill? $"))
tip = float(input("What percentage tip would you like to give ? 10, 12, or 15 "))
people = int(input("How many people to split the bill: "))

total = (bill / people) * (1 + (tip / 100))
new_total = round(total, 2)
print(f"Each person should pay: ${new_total}")
