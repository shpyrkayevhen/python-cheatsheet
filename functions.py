# FUNCTIONS - частина коду, яка виконується при виклику функції
#             необмежену кількість разів з будь якої частини програми.

def question(name: str, country='England') -> str:
    return f'Hello {name}. Are you from {country}'


print(question('Bob'))
print(question('Bob', 'Poland'))

# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


def change(value: dict) -> dict:
    value['name'] = 'Syd'
    return value


val = {'name': 'Beau'}
change(val)  # {'name': 'Syd'} because dict is mutable type

# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# NESTED FUNCTIONS


def talk(phrase: str) -> str:
    def say(word):
        print(word)

    words = phrase.split(' ')
    for word in words:
        say(word)


talk('I am going to buy the car')


def counter() -> int:
    count = 0

    def increment() -> int:
        nonlocal count
        count += 1
        return count

    return increment


increment = counter()

print(increment())  # 1
print(increment())  # 2
print(increment())  # 3

# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# VARIABLE SCOPE

# Global variable
age = 8


def test():
    # Local variable - inside a func not available in global scope only inside a func
    # a = 10
    print(age)


print(age)  # 8
test()  # 8

# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# RECURSION

# 3! = 3 * 2 * 1 = 6
# 4! = 4 * 3 * 2 * 1 = 24
# 5! = 5 * 4 * 3 * 2 * 1 = 120


def factorial(n):
    if n == 1:  # exit point from the recursion
        return 1
    return n * factorial(n-1)


# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# DECORATORS - a function that takes another function and extends
# the behavior of the latter function without explicitly modifying it.

def logtime(func):

    def wrapper(*args, **kwargs):
        print('Do something before')
        val = func()
        print('Do something after')

        return val

    return wrapper


@logtime
def hello():
    print('hello')


hello()


# *args -> tuple, **kwargs -> dict

# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# CLOSING FUNCTION
def main_func(program):

    name = program

    def inner_func():
        print("The best programming language is", name)

    return inner_func


example = main_func('Python')

# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# LAMBDA FUNCTION -> An anonymous function, without a name (Often use with Python functions such as: map, filter, reduce)

# lambda arg : expression -> expression always return value


def multiple(a, b): return a * b


print(multiple(2, 5))
