l = [6, 8, 1, 4, 10, 7, 8, 9, 3, 2, 5]
my_dict = {'py': 'python', 'rb': 'ruby', 'js': 'javascript'}

# sum of all ints
sum = 0
for num in l:
    sum = sum + num

print(f'Sum using list: {sum}')

for num in range(10):
    print(num)

sum = 0
for num in range(len(l)):
    sum = sum + l[num]

print(f'Sum using range genrator: {sum}')

run_times = int(input('How many times do you want to run？'))
for num in range(run_times):
    print(f'Run: {num+1}')

for item in my_dict.items():
    k, v = item
    print(f'Key is {k}, value is {v}')

# generate 100 random intergers between 1 and 100
from random import randint, choice
from string import ascii_lowercase
l1 = []
for num in range(100):
    l1.append(randint(1,100))
print(l1)

l2 = [choice(ascii_lowercase) for num in range(100)]
print(l2)