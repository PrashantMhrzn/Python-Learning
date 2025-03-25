# Methods
# String Methods
value = 'endswithA'

print(value.endswith('A'))
print(value.find('s'))
print(value.swapcase())

# List Methods
lst = [1, 1, 2, 3 ,4]

lst.append('a')
print(lst)

times = lst.count(1)
print(times)

lst.insert(2, 'insert')
print(lst)

lst.pop(3)
print(lst)

# Set
a = {1,2,3,4,5}
b = {4,5,6,7,8}

c = a.difference(b)
print(c)

a.difference_update(b)
print(a)

# Dictionary
a = {'name': 'john', 'age':20, 'city': 'NewYork' }

print(a.items())
print(a.keys())
print(a.values())

print(a.get('name'))
print(a.get('age'))
print(a.get('city'))
