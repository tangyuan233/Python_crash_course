# Strings

print('Hello world I\'m using single quotes')
# Backslash is an escape character and remove the special meaning from the character immediately after it and treat it just as a regular part of the string.
print("Hello world \"using quotes here\" double quotes")

# Variables - memory location references which store values
my_message = 'Hello world using single quotes'
other_message = "Hello world using double quotes"
print(my_message)
print(other_message)

# Python runs from top to down

# Exercises
# Question 1: Use the print function to print the string "Hello World!" (case sensitive)
# write your code below
print("Hello World!")
# end question 1

# Question 2: Use the print function to print the string "Python welcomes you!" (case sensitive)
# write your code below
print('Python welcomes you!')
# end question 2

# Question 3: Use the print function to print the line below, choose single or double quotes appropriately.
# I'm having a great day learning how to code
# write your code below
print('I\'m having a great day learning how to code')
# end question 3

# Question 4: Declare a variable my_message and assign it to the string "Practice makes perfect"
# write your code below
my_message = 'Practice makes perfect'
# end question 4

# Question 5: Use the print function to print the variable my_message you defined above
# write your code below
print(my_message)
# end question 5

# Concatenation - strings can be added to each other
message = 'The price of the stock is:'
print(id(message)) # integer representation of the memory location of objects
price = '$1100'
new_message = message + " " + price
print(new_message)
message = message + " " + price # a new varaible with the same name
print(message)
print(id(message))

# Indexing - reference individual characters in the strings
name = 'interstellar'
print(name[0])
print(name[-2])

# Slicing -  a piece of the strings based on Indexing
# strings[start:stop+1]
print(name[0:5]) # stopping indexing won't be included in the Slicing
print(name[4:]) # from any point of index to the end of String
# strings[start:stop+1:step size]
print(name[1:7:2])
print(name[::-1]) # step size(backward step), reverse


# Methods and functions we can use on string objects
# https://docs.python.org/3/library
# len(), type(), id()
# capitalize(), upper(), lower(), strip(), find()
# split(), join()
# import string
greeting = 'hello'
user = 'xty'
message = '    welcome to the Algorithms course    '
print(greeting.upper(), user.capitalize(), message.strip().lower())
# remove whitespace from before and after the characters in a string
print(len(greeting))
print(len(message))
print(type(greeting))
print(type(5))
print(id(greeting))
print(message.find('course')) # find index of characters in the strings
message = 'welcome-to-the-Algorithms-course'
print(message.split('-'))
my_languages = ['Python', 'Ruby', 'Javascript']
print(' '.join(my_languages))

import string
print(string.ascii_lowercase)

# Question 1: Given the string below, use the find method to determine what index the word "universe" starts in? (and print it)
my_string = "There's a lot going on in the universe don't you think?"
# Write your code below, 1 line #
print(my_string.find('universe'))
# End question 1

# Question 2: Create a variable my_slice. Using a step size of 2, assign it to a slice of my_string from the beginning to the end (the whole string) including white spaces. Print how many characters are in this new string? (my_slice)
# Write your code below, 2 lines #
my_slice = my_string[::2]
print(len(my_slice))
# End question 2

# Question 3: Given the two string below, use string concatenation to
# create and print one string (one followed by the other) seperated by a
# comma and a space ", "
bright_idea = "If we used yesterday's stock price instead"
result = "it would result in a 2% increase in the value of our assets"
# Write your code below, 1 line ##
print(bright_idea + ', ' + result)
# End question 3

# Question 4: You can test whether one string is equal to another by using the equality test operator '=='. For example if you wanted to test whether "Harry" was equal to "Harry", you would use the following code "Harry" == "Harry". Python would evaluate that expression to True (capital T). If you tested if "Harry" == "harry" instead, Python would evaluate that to False (capital F) since "harry" in the second case is not capitalized. Given the string word_to_test below, write and print an equality test in one line to check if the string would be equal to a string if the order of its characters were reversed. Hint: You can use the slice reverse trick.
word_to_test = "level"
# Write your code below, 1 line
reversed_word = word_to_test[::-1]
print(word_to_test == reversed_word)
# End question 4

# Question 5: You can use the len function to get the total characters or 'length' of a string. For example len("hello") will give you 5. If you divide this length by 2 using the floor division operator '//', you can get the index at half of your string. You can then use slice notation to capture half of your string since you know the length//2. With this knowledge, print out the second half of the string below in one line. Output should be "I am the second half".
my_daily_thought = "I am the first half I am the second half"
# Write your code below, 1 line
second_half = len(my_daily_thought)//2
print(my_daily_thought[second_half:])
# End question 5

# Question 6: Import the hexdigits constant from the string module and print them out.
# Write your code below, 2 lines
from string import hexdigits
print(hexdigits)
# End queston 6

# Print formatting and special characters
stock_price = '1100'
print("Today's price for google stock is: " + stock_price)
print("Today's price for google stock is:", stock_price)
print("Today's price for google stock is: {}".format(stock_price)) # take stock_price and insert it
print(f"Today's price for google stock is: {stock_price}") # f-string, evaluate things inside the curly brace
print(f"Today's price for google stock is: {4+5}")
today_price = '1100'
yesterday_price = '1000'
print(f"Today's price: {today_price}, yesterday's price: {yesterday_price}")

# Special characters
# \ - is an escape character, it escapes the special characters following it in a string
# \n - species new line within the string
# \t - adds a tab in it's place within the string
print("My name is jon snow\n\tand not only do I know nothing but\\n\tI also do nothing")
