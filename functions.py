# FUNCTIONS - частина коду, яка виконується при виклику функції
#             необмежену кількість разів з будь якої частини програми.

def hello(name: str, country='Ukraine') -> str:
    return f'Hello {name}. Are you from {country}'


print(hello('Bob'))
print(hello('Bob', 'Poland'))


# *args -> tuple, **kwargs -> dict
def func(*args, **kwargs):
    pass
