# Polymorphism

from telnetlib import DO


class Dog:

    def eat(self):
        print('Eating dog Food')


class Cat:

    def eat(self):
        print('Eating cat Food')


animal1 = Dog()
animal2 = Cat()

animal1.eat()
animal2.eat()
