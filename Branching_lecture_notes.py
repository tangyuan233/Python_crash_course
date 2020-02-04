# Branching: If, elif, else
# Conditionals evaluating to Boolean - True or False
# if condition:    
#   execute some code
# elif other_condition:   
#   execute some other code
# else:
#   execute some other code

# Booleans and conditions
# Evaluate to True or False (Boolean)
# 1. greater than >
# 2. less than <
# 3. greater than or equal to >=
# 4. less than or equal to <=
# 5. equal to ==
# 6. not equal to !=

choice = input('Choose to multiply, 2 to divide-> ')
if choice == '1' or choice == '2':
    num_1 = int(input('Enter first number-> '))
    num_2 = int(input('Enter second number-> '))
    if choice == '1':
        print(f'{num_1} multiplied by {num_2} is: {num_1*num_2}')
    elif choice == '2':
        print(f'{num_1} divided by {num_2} is: {num_1/num_2}')
else:
    print("You've made an invalid selection")