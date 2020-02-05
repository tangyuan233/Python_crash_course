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

choice = input('Choose 1 to multiply, 2 to divide-> ')
if choice == '1' or choice == '2':
    num_1 = int(input('Enter first number-> '))
    num_2 = int(input('Enter second number-> '))
    if choice == '1':
        print(f'{num_1} multiplied by {num_2} is: {num_1*num_2}')
    elif choice == '2':
        print(f'{num_1} divided by {num_2} is: {num_1/num_2}')
else:
    print("You've made an invalid selection")

made_payment = True
a = 'Please pay monthly premium'
b = 'Welcome to your homepage'

if not made_payment:
    print(a)
else:
    print(b)

print(a) if not made_payment else print(b)

i = 10
j = 10
k = 10
if i < j and i < k:
    print('i is less than j and k')
elif i == j and i == k:
    print('i is equal to j and k')
elif i == j or i == k:
    print('i is equal to either j or k')
else:
    print('something else')

course = 'python'
a = 'enrolled in python course'
b = 'enrolled in some other course'
print(a) if course == 'python' else print(b)

# Question 1: Write an if/else condition to print "Access granted"
# if the account variable is equal to the string "verified" AND
# payment_status is "paid". Else print "Access denied".
account = "verified"
payment_status = "paid"
# Write your code below (variable number of lines)
print('Access granted') if account == 'verified' and payment_status == 'paid' else print(
    'Access denied')

# End question 1

# Question 2: Modify your code above and introduce a check for
# if account == "verified" and payment_status == "pending", then
# print "Temporary access granted, check payment status", if the
# payment status does not match either "pending" or "paid" (and
# the account is still verified) then print "Access denied, check payment".
# Other conditions from question 1 above still apply.
account = "verified"
payment_status = "pending"
# Write your code below (variable number of lines)
if account == 'verified' and payment_status == 'pending':
    print('Temporary access granted, check payment status')
elif account == 'verified' and (payment_status != 'pending' or payment_status != 'paid'):
    print('Access denied, check payment')


# Copy/paste your code (entire block for question 2) below, this
# if for a separate test for payment_status
payment_status = "blocked"
if account == 'verified' and payment_status == 'pending':
    print('Temporary access granted, check payment status')
elif account == 'verified' and (payment_status != 'pending' or payment_status != 'paid'):
    print('Access denied, check payment')

# End question 2

# Question 3: Write an if/elif/else condition to check for the 3 account
# types below and print the corresponding statement. If account type
# matches none of these then it should print "Access denied"
# a) account_type == "admin", should result in print "Admin access"
# b) account_type == "mod", should result in print "Moderator access"
# c) account_type == "user", should result in print "User access"
account_type = "user"
# Write your code below (variable number of lines)
if account_type == 'admit':
    print('Admin access')
elif account_type == 'mod':
    print('Moderator access')
elif account_type == 'user':
    print('User access')

# End question 3
