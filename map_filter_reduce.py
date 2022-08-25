from functools import reduce

# 1: map(func, iterable_collection)

numbers = [1, 2, 3]

result = map(lambda num: num * 2, numbers)

print(list(result))

# The same result use list compressions

result = [num * 2 for num in numbers]

print(result)

# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# 2: filter() -> return if expression is True

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

result = filter(lambda num: num % 2 == 0, numbers)
print(list(result))

# The same result use list compressions

result = [num for num in numbers if num % 2 == 0]
print(result)

# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# 3: reduce() - коли потрібно підрахувати значення елементів вихідних колекцій

# Example without reduce func

expenses = [('Dinner', 80), ('Car repair', 10)]

sum = 0

for expense in expenses:
    sum += expense[1]

# Example using reduce
# from functools import reduce

sum = reduce(lambda a, b: a[1] + b[1], expenses)
print(sum)
