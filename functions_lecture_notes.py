# Structure of functions
# def name_of_func():
    # code to perform function operations must be indented to be considered part of the function

# Notes on functions
# 1. May or maynot include parameters
# 2. Might have return value specified, otherwise returns None by default
# 3. Good to include a docstring in the function to provide information about it
# 4. Try to limit a function to perform only 1 defined function, for example: an add function should only perform addition, not addition and multiplication
# 5. Functions can return multiple values (as tuples)

# include parameters, return interger
def add_two_nums(num_1, num_2):
    return num_1 + num_2

# does not include, return value none
def say_hello():
    '''This funciton prints hello world'''
    print('Hello World')

print(add_two_nums(5,6))

result = add_two_nums(5,6)
print(result)

say_hello()
print(say_hello())

def func_0(start_num):
    start_num += 1
    return func_1(start_num)

def func_1(start_num):
    start_num += 1
    return start_num

start_num = 1
print(f'start_num\t-> {start_num}')
finish_num = func_0(start_num)
print(f"calc'd_num\t-> {finish_num}")
print(f'start_num\t-> {start_num}')
print(finish_num == start_num)


def func_0(other_num):
    other_num[0] += 1
    return func_1(other_num)

def func_1(another_num):
    another_num[0] += 1
    return another_num  

start_num = [1]
print(f'start_num\t-> {start_num}')
finish_num = func_0(start_num)
print(f"calc'd_num\t-> {finish_num}")
print(f'start_num\t-> {start_num}')
print(finish_num == start_num)
