# Things you can do with lists
# 1. sort the values in ascending order, descending order 
#   - sort(), sorted()
# 2. find values in the list, or details about the list 
#   - len(), min(), max(), in, indexing, slicing, count()
# 3. insert or remove values from the list (including other lists) 
#   - append(), insert(), extend(), remove(), pop()
# 4. grab sub-lists from the list to work with 
#   - slicing, in-place, copying
# 5. iterate through and perform functions / checks on each list item 
#   - for loops, while loops

my_list = [15, 6, 7, 8, 35, 12, 14, 4, 10]
my_strings_list = ['comp sci', 'physics', 'elec engr', 'philosophy']
print(f'Ints: {my_list}')
print(f'Strings: {my_strings_list}')
print(id(my_list))
my_list.sort()
print('Sorting...')
sorted_list = sorted(my_list)
print(id(sorted_list))
print(id(my_list))
print(f'Sorted Ints: {my_list}')

print('Finding info...')
print('physics' in my_strings_list)
print(my_strings_list.index('philosophy'))
print(len(my_strings_list))
print(my_list[len(my_list)-1])
print(my_list[-1])
print(min(my_list))
print(max(my_list))
print(dir(my_list))
print(my_list.count(1))

# Question 1: Given the list below, print the min value from the list using the
# min function
my_list = [903, 373, 223, 4031, 2033, 535, 677, 601, 403,
           340, 370, 352, 441, 293, 567, 8888, 1031, 788, 161]
# Write your code below, 1 line
print(min(my_list))
# End question 1

# Question 2: Given the list below, using the 'in' operator, print (True or False) if
# 'urgent' exists in the list.
my_words_list = ['extreme', 'arrow', 'urgently',
                 'important', 'Urgent', 'imperative']
# Write your code below, 1 line
print('urgent' in my_words_list)
# End question 2

# Question 3: Use the sorted function to sort my_list from question 1 and assign it to a variable
# named my_sorted_list
# Write your code below, 1 line
my_sorted_list = sorted(my_list)
# End question 3

# Question 4: Use the sort method to sort my_list from above and print out my_list below it
# Write your code below, 2 lines
my_list.sort()
print(my_list)
# End question 4

# Question 5: Use the equality test to check if my_sorted_list is equal to my_list. Remember
# to print the result.
# Write your code below, 1 line
print(my_sorted_list == my_list)
# End question 5

# append(), insert(), extend()
my_list = [15, 6, 7, 8, 35, 12, 14, 4, 10]
# indices  0   1  2  3   4   5   6  7   8
my_strings_list = ['comp sci', 'physics', 'elec engr', 'philosophy']
my_new_list = ['art', 'econ']
my_list.append(25)
print(my_list)
my_list.insert(4, 25) # (index, value)
print(my_list)
my_strings_list.extend(my_new_list) # add list to a list
print(my_strings_list)

# pop(), remove()
my_strings_list.remove('comp sci')
print(my_strings_list)
print(my_strings_list.pop()) # remove last object, return what is removed

my_list[-1] = 1000
print(my_list)
print(my_list[0:4]) # stop index is not included
print(my_list[::-1]) # reversed list
my_list.reverse()
print(my_list)

for item in my_list:
    print(item)

# Question 1: Given the two lists below, add all the elements in the second list
# to the end of the first list, then print out the first list. Choose the
# appropriate method to add these elements so that you don't end up with a list
# within a list (as in the first list 'my_courses' should only have string data,
# not lists of strings).
my_courses = ['comp sci', 'economics', 'physics', 'astronomy']
new_courses = ['climate studies', 'artificial intelligence']
# Write your code below, 2 lines ##
my_courses.extend(new_courses)
print(my_courses)
# End question 1

# Question 2: Given the string below, add it to the end of my_courses list which
# you printed at the end of question 1, then print out my_courses
new_course = 'tennis'
# Write your code below, 2 lines
my_courses.append(new_course)
print(my_courses)
# End question 2

# Question 3: Choose the approprite method to delete 'economics' from my_courses
# list and print the resulting my_courses list.
# Write your code below, 2 lines
my_courses.remove('economics')
print(my_courses)
# End question 3

# Question 4: Given the integer list below, print the length of the list (number
# of integers in the list).
my_int_list = [9, 6, 13, 7, 27, 99, 104, 100, 10, 16, 42, 64]
# Write your code below, 1 line
print(len(my_int_list))
# End question 4

# Question 5: Grab the second half of my_int_list using slice notation and print
# it to the screen
# Write your code below, 1 line
print(my_int_list[6:])
# End question 5
