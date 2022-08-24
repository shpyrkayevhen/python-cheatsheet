# ARITHMETIC OPERATORS

1 + 1  # 2
2 - 1  # 1
2 * 2  # 4
4 / 2  # 2 -> type(float)
4 % 3  # 1
4 ** 2  # 16
5 // 2  # 2

# Combine Arithmetic Operators with assign: += / -=/ *= /
age = 8
age += 5  # age = age + 8

# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# COMPARISON OPERATORS

a = 1
b = 2

a == b  # False
a != b  # True
a > b  # False
a <= b  # True

# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# BOOLEAN OPERATORS

condition1 = True
condition2 = False

not condition1             # False
condition1 and condition2  # False
condition1 or condition2   # True

print(0 or 1)  # 1
print(False or 'hey')  # 'hey'
print('hi' or 'hey')  # 'hi'
print([] or False)  # False
print(False or [])  # []

print(0 and 1)  # 0
print(1 and 0)  # 0
print(False and 'hey')  # Fasle
print('hi' and 'hey')  # 'hi'
print([] and False)  # []
print(False and [])  # False

# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# is & in OPERATORS

# in: membership operator
lst = [5, 7, 10]
print(5 in lst)  # True

# is:s
print(lst is not None)  # True

# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# TERNARY OPERATORS

age = 10

if age >= 10:          # True
    print('True')
elif age == 30:
    print('Yep')
else:
    print('False')


def is_adult(age: int) -> bool:
    return True if age > 18 else False


is_adult(10)  # True

# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# BITWISE OPERATORS

# & performs binary AND
# | performs binary OR
# ^ performs a binary XOR operation
# ~ performs a binary NOT operation
# << shift left operation
# >> shift right operation
