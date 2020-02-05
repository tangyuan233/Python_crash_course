# Lists
node_1 = 'custom object'

my_data_type = [1, 2, False, 4, 'mashrur', None, node_1, 5.0, 1]
print(my_data_type[-2])
print(type(my_data_type))

# Dictionaries
my_data_type = {1: 'hello', 2:'mashrur', 3: None, 4: node_1, 5: 5.0}
print(my_data_type[3])
print(type(my_data_type))

# Sets
my_data_type = {1, 2, False, 4, 'mashrur', None, node_1, 5.0, 1} # sets don't allow duplicate values
print(my_data_type) # no ordering , no index
print(type(my_data_type))

# Tuples
my_data_type = (1, 2, False, 4, 'mashrur', None, 5.0)
print(my_data_type[5])
# my_data_type[5] = 'python # tuples are immutable
print(type(my_data_type))
