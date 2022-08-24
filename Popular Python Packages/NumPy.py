# When we work with large, multi dimensional arrays
# pip install numpy
from this import d
import numpy as np


# Creatin an array -> return numpy array
array = np.array([1, 2, 3])
print(array)


# Creatin multi dimensional array (called matrix in math)
array = np.array([[1, 2, 3], [4, 5, 6]])

# Will get information in tuple (2, 3) -> 2 rows, 3 column
print(array.shape)

# Create array (3 rows(lis), 4 colums(elemet)) -> values 0
array = np.zeros((3, 4), dtype=int)
print(array)

# values 1
array = np.ones((3, 4), dtype=int)
print(array)

# input numbers which we need (5)
array = np.full((3, 4), 5, dtype=int)
print(array)

# creating array with random values
array = np.random.random((3, 4))
print(array)

# access elements by index
print(array[1, 3])


# !! VERY POWETFULL THING !!
# print(array > 0.5)


# Поверне лише ті елементи, які True
# print(array[array > 0.5])

# Поверне суму всіх елементів array
# print(np.sum(array))

# print(np.floor(array))
# print(np.ceil(array))
# print(np.round(array))

# Можемо виконувати різні арифметичні операції між різними масивами
first = np.array([1, 2, 3])
second = np.array([1, 2, 3])

# return -> [2, 4, 6]
print(first + second)

# return -> [3, 4, 5]
print(first + 2)

# Хочемо конвертувати всі значення array в см.
dimensions_inch = np.array([1, 2, 3])
dimensions_cm = dimensions_inch * 2.54
