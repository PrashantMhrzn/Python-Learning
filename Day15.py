# OOP

# Requierments
# create a class called dog
# should have attributes to define dog objects and methods like move, eat, get_legs, get_name
class Dog:
    def __init__(self):
        self.name = 'Brown'
        self.breed = 'Husky'
		
    def move(self, direction):
        print(f'{self.name} moved to {direction}!')

    def eat(self, *food):
        count = 0
        for i in food:
            count += 1
        print(f'{self.name} ate {count} times')

# hus = Dog()
# print(hus.name)
# print(hus.breed)
# hus.move('south')
# hus.eat('meat', 'rice', 'bones')

# Inheritance
class Parent:
    height = 180
    eyes = 'blue'
    build = 'muscular'

# Polymorphism