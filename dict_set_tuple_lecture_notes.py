# Dictionaries
from collections import OrderedDict

my_dictionary = {'name': 'mashrur', 'course': 'python', 'fav_food': 'ice cream'}

phone_dict = {'mashrur': '555-55-5555', 'zoolander': '999-99-9999', 'jon_snow': 'fail-o-so-bad'}

word_dict = {
    'a': {
        'apple': 'the round first of a tree of the rose family',
        'ant': 'an insect which cleans up the floor'
    },
    'b': {
        'bad': 'of poor quaity or low standard',
        'business': 'season 8 of GOT'
    }
}

print(my_dictionary)
print(word_dict['b']['business'], word_dict['b']['bad'])
print(my_dictionary.get('name'))

my_dictionary['job'] = 'python programming'
print(my_dictionary.get('job'))

print(my_dictionary.keys())
print(my_dictionary.values())
print(my_dictionary.items())

for k, v in my_dictionary.items():
    print(k, v)

# Question 1: Create an empty dictionary called life_book of type OrderedDict.
# From Python 3.6 onwards dictionaries maintain the order in which they were
# created, however, this coding environment uses an earlier version of Python 3.
# Therefore, use OrderedDict in this case, example my_dict = OrderedDict().
# Once created, use the print function to print it.
# Write your code below, 2 lines
life_book = OrderedDict()
print(life_book)
# End question 1

# Question 2: Add the following key, value pair to the life_book dictionary
# 'pet' -> 'dog', so the key is pet and the value is dog and then print it.
# Write your code below, 2 lines
life_book['pet'] = 'dog'
print(life_book)
# End question 2

# Question 3: Add the following key, value pairs to the dictionary
# 'second_pet' -> 'cat'
# 'first_child' -> 'boy'
# 'second_child' -> 'girl'
# Once added, print the dictionary.
# Write your code below, variable lines
life_book['second_pet'] = 'cat'
life_book['first_child'] = 'boy'
life_book['second_child'] = 'girl'
print(life_book)
# End question 3

# Question 4: Update the value associated with key 'pet' to be 'hamster', then
# print the dictionary.
# Write your code below, 2 lines
life_book['pet'] = 'hamster'
print(life_book)
# End question 4

# Question 5: Given the dictionary below, use the items() method and save
# the value of all the key value pairs to the variable courses_iterable.
my_courses = {'a': 'python', 'b': 'javascript',
              'c': 'ruby on rails', 'd': 'machine learning', 'e': 'ai'}
# Write your code below, 1 line
courses_iterable = my_courses.items()
# End question 5


# Tuples # immutable
my_random_tuple = ('first', 1, 7, 6, 4, 5, 8, 'hi there', 2, 3, 1, 5, 2, 1, 9, 10)
my_tuple = ('first_value', 'second_value', 'third_value')

print(my_random_tuple[2])
print(my_random_tuple[::-1])

print(len(my_random_tuple))
print(my_random_tuple.count(2))
print(my_random_tuple.index('hi there'))

first_var, second_var, third_var = my_tuple
print(third_var)

print('first' in my_random_tuple)
for item in my_random_tuple:
    print(item)

# Sets
my_set = {1, 6, 2, 'java', 'ruby', 8, 9, 10, 21, 1000, 'python', 6}
my_list = [1, 6, 2, 'java', 'ruby', 8, 9, 10, 21, 1000, 6, 'python', 'java']
print(my_list)
my_set = set(my_list)
print(my_set)
print('java' in my_set)

programming_set = {'jave', 'ruby', 'javascript', 'python', 'c'}
print(my_set.intersection(programming_set))  # find intersection between tow sets
print(my_set.union(programming_set))
print(my_set.difference(programming_set))


# Question 1: Create an empty set called my_ints, once it's created
# use the type function (along with print) to print the type of my_ints.
# Write your code below, 2 lines
my_ints = set()
print(type(my_ints))
# End question 1

# Question 2: Given the list below, convert it to a set named my_set and then
# cast it back to a list called my_unique_list which only includes unique
# elements. No print required.
my_list = [1,1,'rails',7,6,2,'java','ruby',8,9,10,21,'rails',7,2,1000,6,'python','java']
# Write your code below, 2 lines
my_set = set(my_list)
my_unique_list = list(my_set)
# End question 2

# Question 3: Add the int 8 to my_ints you created in question 1. Print the
# output when you run the intersection method on my_ints and pass it my_set
# (created in question 2) as the argument.
# Write your code below, 2 lines
print(my_ints.add(8))

# End question 3

# Question 4: Test (and print) if 'rails' is in my_set
# Write your code below, 1 line
print('rails' in my_set)
# End question 4

# Question 5: Given the tuple below, use a simple for loop and print out all
# the elements in it (no special formatting).
my_random_tuple = ('first',4,5,8,'hi there',5,2,1,9,10)
# Write your code below
for item in my_random_tuple:
    print(item)
# End question 5