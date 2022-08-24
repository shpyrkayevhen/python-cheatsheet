done = True

if done:
    print('yes')
else:
    print('no')

if not done:
    print('yes')
else:
    print('no')


# ALWAYS FALSE VALUE: 0, empty string, list, touple, dictionary('', {}, []), None

# NEGATIVE NUMBERS IS TRUE !!!

print(type(done) == bool)  # False

# GLOBAL FUNCTIONS

# any() - return True if at least one element is True
read_any_books = any([0, 'Python', []])  # True

# all() - return True if all element is True
read_all_books = all([0, 'Python', []])  # False
