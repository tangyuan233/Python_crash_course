from random import randint
5# Numbers - Intergers, floats

# Math
# Interger - whole number, no decimal
print(type(4))
print(type(3.5))
result = 4 + 4
print(type(result))
print(result)
print(result + 4)
print(abs(-10))
result = 10  /5
print(type(result))
result = 10 // 3 # floor division, drops the decimal
print(type(result))
print(type(10 + 2.0)) # anytime you introduce a float in to the mix, the result is going to be a float
print(type(10 % 3)) # reminder
print(10 % 2) # test a numner is even or not, even - 0, odd - 1
print(5 ** 2) # 5 to the power of 2, square
print(5 ** 3)
import math
print(math.pow(10,5))
print(math.log2(1000000))
import random
print(random.randint(0,1000))

# Type Casting
num_1 = "10"
num_2 = "20"
result = num_1 + num_2 # cannot add int to str
print(type("10"))
print(result)
print(type(int(result)))

# Getting input from user
print("Welcome to the multiplication program")
print("-"*30)
num_1 = int(input("Enter a number to multiply -> "))
num_2 = int(input("Enter a second number to multiply -> "))
result = num_1 * num_2
print(result)

# Question 1: What is the remainder when you divide 2510876961 by 7?
# Don't forget to print your result to the screen!
num_1 = 2510876961
num_2 = 7
# Fill in your code below, 1 line ##
remainder = num_1 % num_2
print(remainder)
# End question 1

# Question 2: Python will place a higher order of importance to operations specified within parenthesis. 
# If you are given the 3 numbers below and asked to add the first two numbers first, then divide by the third one, uncomment the line below that provides the right result
num_1 = 15
num_2 = 25
num_3 = 100
# Uncomment the correct line below based on the question above
# print(num_1 + num_2 / num_3)
# print(num_1 / num_2 + num_3)
# print(num_1 + (num_2 / num_3))
print((num_1 + num_2) / num_3)
# End question 2

# Question 3: Import the randint function from the random module so it can be used by it's name, randint, instead of referring to the random module first
# Write your code below, 1 line ##
my_num = randint(5, 100)
# End question 3
