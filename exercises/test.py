# # Python by Example Book - exercises

### IF STATEMENTS CHALLENGES ###

# # Challenge 012
# num1 = int(input("Enter first number: "))
# num2 = int(input("Enter second number: "))
# if num1 > num2:
#     print(num2, num1)
# else:
#     print(num1, num2)

# # Challenge 013
# num = int(input("Enter a number that is under 20: "))
# if num > 20:
#     print("The number you entered is too high. Pleas43e, try again!")
# else:
#     print("Thank you!")

# Challenge 014
# num = int(input("Please, enter a number between 10 and 20 - inclusive: "))
# if num >= 10 and num <= 20:
#     print("Thank you!")
# else:
#     print("Incorrect answer")

# # Challenge 015
# color = input("Enter your favorite colour: ")
# if color == "red" or color == "RED" or color == "Red":
#     print("I like red too!")
# else:
#     print("I don't like that color, I prefer red")

# # Challenge 016
# user = input("It is raining outside? ")
# user = str.lower(user)
# if user == "yes":
#     windy = input("Is it windy? ")
#     windy = str.lower(windy)
#     if windy == "yes":
#         print("It is too windy for an umbrella!")
#     else:
#         print("Take an umbrella!")

# else:
#     print("Enjoy your day!")

# # Challenge 017
# age = int(input("How old are you? "))
# if age >= 18:
#     print("You can vote")
# elif age == 17:
#     print("You can learn to drive")
# elif age == 16:
#     print("You can buy a lottery ticket")
# else:
#     print("You can go Trick-or-Treating")

# # Challenge 018
# num = int(input("Enter a number: "))
# if num < 10:
#     print("Too low")
# elif num >= 10 and num <= 20:
#     print("Correct!")
# else:
#     print("Too high")

# # Challenge 019
# num = int(input("Enter the number 1, 2 or 3: "))
# if num == 1:
#     print("Thank you!")
# elif num == 2:
#     print("Well done!")
# elif num == 3:
#     print("Correct")
# else:
#     print("Error messsage")

### STRINGS CHALLENGES ###

# # Challenge 020
# name = input("Enter your name: ")
# length = len(name)
# print(length)

# # Challenge 021
# firstname = input("Enter your name: ")
# lastname = input("Enter you lastname: ")
# name = firstname + " " + lastname
# length = len(name)
# print(name)
# print(length)

# # Challenge 022
# firstname = input("Enter your name in lower case: ")
# lastname = input("Enter you lastname in lower case: ")
# name = firstname + " " + lastname
# cap = name.title()
# print("Your lower case name: ", name)
# print("Here the title case: ", cap)

# # Challenge 023
# rhyme = input(
#     "If you remember it, enter the first line of a nursery rhyme: ")
# length = len(rhyme)
# start_num = int(input("Enter a starting number: "))
# last_num = int(input("Enter a ending number: "))
# part = (rhyme[start_num: last_num])
# print(part)

# # Challenge 024
# word = input("Type any word you like: ")
# upper = word.upper()
# print(upper)

# # Challenge 025
# firstname = input("Please enter your name: ")
# if len(firstname) < 5:
#     surname = input("Enter your surname: ")
#     name = firstname + surname
#     print(name.upper())
# else:
#     print(firstname.lower())

# # Challenge 026
# word = input("Enter a word: ")
# first_word = word[0]
# length = len(word)
# rest = word[1:length]
# if first_word != "a" and first_word != "e" and first_word != "i" and first_word != "o" and first_word != "u":
#     new_word = rest + first_word + "ay"
# else:
#     new_word = word + "way"
# print(new_word.lower())


# # MATHS CHALLENGES
# # Challenge 027 & 028
# num = float(input("Enter a number with lots of decimal places: "))
# answer = num * 2
# print(answer)
# print(round(answer, 2))

# # Challenge 029
# import math
# num = int(input("Enter an integer that is over 500: "))
# answer = math.sqrt(num)
# print(round(answer, 2))

# # Challenge 030
# import math
# print(round(math.pi, 5))

# # Challenge 031
# import math
# radius = int(input("Enter the radius of a circle: "))
# area = math.pi * (radius**2)
# print(area)

# # Challenge 032
# import math
# radius = int(input("Enter the radius of a circle: "))
# depth = int(input("Enter the depth of a cylinder: "))
# area = math.pi * (radius**2)
# total_volume = area * depth
# print(round(total_volume, 3))

# # Challenge 033
# import math
# num1 = int(input("enter a number: "))
# num2 = int(input("enter another number: "))
# div = num1 // num2
# remainder = num1 % num2

# print(num1, "divided by", num2, "is", div, "with", remainder, "remaining")

# # Challenge 034
# print("""
# 1) Square
# 2) Triangle
# """)
# num = (int(input("Enter a number: ")))
# if num == 1:
#     square = int(input("Provide the length of one of the square sides: "))
#     area = square * square
#     print("The area of your square is", area)
# elif num == 2:
#     base = int(input("Provide the base of the triangle: "))
#     height = int(input("and the height of the triangle: "))
#     area = (base * height) / 2
#     print("The area of your triangle is", area)
# else:
#     print("Please, choose a number between the two options")

### FOR LOOP CHALLENGES ###

# # Challenge 035 & 36
# name = input("Enter your name: ")
# num = int(input("Enter a number: "))
# for i in range(0, num):
#     print(name)

# # Challenge 037 & 038
# num = int(input("Enter a number: "))
# name = input("Enter your name: ")
# for x in range(0, num):
#     for i in name:
#         print(i)


# # Challenge 039
# num = int(input("Enter a number between 1 and 12: "))
# for i in range(1, 13):
#     answer = i * num
#     print(i, "x", num, "=", answer)

# Challenge 040
# Challenge 041
# Challenge 042
# Challenge 043
# Challenge 044


### WHILE LOOP CHALLENGES ###

# Challenge 045
