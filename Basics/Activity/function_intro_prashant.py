# todo:
# ask user for name, age, address, ....
# create a function with parameters
# print out a introduction of the user using function
# print introduction of 3 users

def intro(name, address, age=18):
    print(f'Hi! my name is {name}. I am {age} years old. I live in {address}')

intro('shyam', 'thamel', 20)
intro('raam', 'sundhara')
intro('hari', 'thamel', 27)