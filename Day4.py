# Type Conversion/Casting

my_str = "123" 
int(my_str)
print(type(my_str))

my_con_list = "12345abccc"

# Converting into list
my_con_list = list(my_con_list)
print(my_con_list)

# Converting into tuple
my_con_list = tuple(my_con_list)
print(my_con_list)

# Converting into set
my_con_list = set(my_con_list)
print(my_con_list)

# Converting into dict
# List of Tuple into Dictionary
my_dict_list = [(1, 'ram'), (2, 'shyam'), (3, 'bham')]

my_dict_list = dict(my_dict_list)
print(my_dict_list)

# Activity - Change values of tuple by type conversion
to_change_tuple = ("apple","banana","kiwi","orange","cat")
print(to_change_tuple)
# Change to list
tup_to_lst = list(to_change_tuple)

# Change data
tup_to_lst[4] = "mango"

# Change to tuple
lst_to_tup = tuple(tup_to_lst)

print(lst_to_tup)
