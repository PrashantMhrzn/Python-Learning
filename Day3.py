# Indexing and Sclicing
# String
# [Starting_index: Ending_index: Step]

sen = "I am a ( programmer."

print(sen[::-1])

# List indexing
my_list = ['a', 'b', 'c', 'd']
print(my_list)

# Changing values
my_list[3] = "Donald"
print(my_list)

print(my_list[::2])

# Activity: Make a list of your hobbies, print a sentence like "I like <list data>" using indexing
my_hobbies = ['Playing Guitar', 'Cooking', 'Coding']

for i in range(len(my_hobbies)):
    print(f"I like {my_hobbies[i]}")


for i in my_hobbies:
    print(f"I like { i }")

    pass

my_hobbies_tuple = ['Playing Guitar', 'Cooking', 'Coding']

print(my_hobbies_tuple[2])
print(my_hobbies_tuple[0:2])






