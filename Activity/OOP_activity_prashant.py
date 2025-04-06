# Requirments
# create a class named animal with attributes like legs, eyes, ear, methods like eat, sleep,....
# create a class named cat that inherits animal class, add other attributes like name, age.... and methods like sound
# create its objects

class Animal:
    legs = 4
    eyes = 'blue'
    ears = 'sharp'
    name = 'animal'
        
    def sleep(self, time):
        print(f'{self.name} slept for {time}!')

    def eat(self, *food):
        count = 0
        for i in food:
            count += 1
        print(f'{self.name} ate {count} times')


class Cat(Animal):
    name = 'Ariana'
    age = 5

    def sound(self):
        print('meow')

c1 = Cat()
c1.sleep('5 minutes')
c1.eat('fish', 'trout')
c1.sound()

a1 = Animal()

print(c1.ears)
print(c1.name)
print(c1.age)
print(a1.name)
print(c1.legs)

