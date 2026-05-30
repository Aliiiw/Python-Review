# # # # # # # a = 33
# # # # # # # b = 200
# # # # # # # if b > a:
# # # # # # #     print("b is greater than a")


# # # # # # # age = 20
# # # # # # # if age >= 18:
# # # # # # #     print("You are an adult")
# # # # # # #     print("You can vote")
# # # # # # #     print("You have full legal rights")


# # # # # # a = 33
# # # # # # b = 33
# # # # # # if b > a:
# # # # # #     print("b is greater than a")
# # # # # # elif a == b:
# # # # # #     print("a and b are equal")


# # # # # score = 75

# # # # # if score >= 90:
# # # # #     print("Grade: A")
# # # # # elif score >= 80:
# # # # #     print("Grade: B")
# # # # # elif score >= 70:
# # # # #     print("Grade: C")
# # # # # elif score >= 60:
# # # # #     print("Grade: D")


# # # # age = 25

# # # # if age < 13:
# # # #     print("You are a child")
# # # # elif age < 20:
# # # #     print("You are a teenager")
# # # # elif age < 65:
# # # #     print("You are an adult")
# # # # elif age >= 65:
# # # #     print("You are a senior")

# # # day = 3

# # # if day == 1:
# # #     print("Monday")
# # # elif day == 2:
# # #     print("Tuesday")
# # # elif day == 3:
# # #     print("Wednesday")
# # # elif day == 4:
# # #     print("Thursday")
# # # elif day == 5:
# # #     print("Friday")
# # # elif day == 6:
# # #     print("Saturday")
# # # elif day == 7:
# # #     print("Sunday")

# # a = 200
# # b = 33
# # if b > a:
# #     print("b is greater than a")
# # elif a == b:
# #     print("a and b are equal")
# # else:
# #     print("a is greater than b")

# # a = 200
# # b = 33
# # if b > a:
# #     print("b is greater than a")
# # else:
# #     print("b is not greater than a")


# # username = "Emil"
# # password = "python123"
# # is_active = True

# # if username:
# #     if password:
# #         if is_active:
# #             print("Login successful")
# #         else:
# #             print("Account is not active")
# #     else:
# #         print("Password required")
# # else:
# #     print("Username required")


# # age = 16

# # if age < 18:
# #     pass  # TODO: Add underage logic later
# # else:
# #     print("Access granted")

# # day = 4
# # match day:
# #     case 1:
# #         print("Monday")
# #     case 2:
# #         print("Tuesday")
# #     case 3:
# #         print("Wednesday")
# #     case 4:
# #         print("Thursday")
# #     case 5:
# #         print("Friday")
# #     case 6:
# #         print("Saturday")
# #     case 7:
# #         print("Sunday")

# # day = 4
# # match day:
# #     case 6:
# #         print("Today is Saturday")
# #     case 7:
# #         print("Today is Sunday")
# #     case _:
# #         print("Looking forward to the Weekend")

# day = 4
# match day:
#     case 1 | 2 | 3 | 4 | 5:
#         print("Today is a weekday")
#     case 6 | 7:
#         print("I love weekends!")
