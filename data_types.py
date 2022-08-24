# IMMUTABLE TYPES
name = 'Python'                 # str
age = 5                         # int
price = 255.55                  # float
statement = True or False       # boolean
tpl = (True, 10, 'Django')      # tuple
rng = range(1, 10)              # range


# MUTABLE TYPES
lst = ['Python', [], 25, True]   # list
dct = {'key': 'value'}           # dictionary
unique = {1, 2, 3}               # set (disordered)


# Check The Data Type
print(type(name))
print(isinstance(name, str))

# Convert Data Type (Casting)
number = '20'
age = int(number)
print(isinstance(age, int))  # True
