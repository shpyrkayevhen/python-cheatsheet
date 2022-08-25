# Operator Overloading

from telnetlib import DO


class Dog:

    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def __gt__(self, other):
        return True if self.age > other.age else False


roger = Dog('Roger', 10)
indi = Dog('Indi', 5)

print(roger > indi)  # True

# __eq__() to check for equality
# __lt__() to check if an object should be considered lower than another with the < operator
# __le__() for lower or equal (<=)
# __ge__() for greater or equal (>=)
# __ne__() for not equal (!=)

# Methods to interoperate with arithmetic operations:

# __add__() respond to the + operator
# __sub__() respond to the – operator
# __mul__() respond to the * operator
# __truediv__() respond to the / operator
# __floordiv__() respond to the // operator
# __mod__() respond to the % operator
# __pow__() respond to the ** operator
# __rshift__() respond to the >> operator
# __lshift__() respond to the << operator
# __and__() respond to the & operator
# __or__() respond to the | operator
# __xor__() respond to the ^ operator
