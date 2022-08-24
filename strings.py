# STRINGS(str) - упорядкований набір сиволів. IMMUTABLE TYPES. ITERABLE OBJ.
name = 'Indi'
city = 'Lviv'

# Concatenation
print(name + ' is from ' + city)

# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# STRING METHODS

name = 'indi'

name.title()  # Indi
name.upper()  # INDI
name.lower()  # indi
name.isupper()  # False
name.islower()  # True
name.count('i')  # 2
name.startswith('i')  # True
name.endswith('i')  # True
name.replace('i', 'a')  # anda
name.split()  # to split a string on a specific character separator
name.strip()  # to trim the whitespace from a string
name.find('i')  # [0]
name.join()  # to append new letters to a string
name.isalpha()  # true
name.isdecimal()  # to check if a string contains digits and is not empty
name.isalnum()  # to check if a string contains characters or digits and is not empty

# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# GLOBAL FUNCTIONS

len(name)  # 4
'in' in name  # True

# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# ESCAPING CHARACTERS
name = 'in\'di'
name = 'In\ndi'  # new line
name = r'In\ndi'  # In\ndi
print(name)

# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# STRING CHARACTERS / SLICING

name[0]  # 0
name[0:4]  # ind
name[-1]  # the last characters
name[0:5:2]  # id

# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# FORMATING STRING

print(f'Hello {name}. Are you from {city}')
print('Hello %s. Are you from %s' % (name, city))
