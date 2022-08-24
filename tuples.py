# TUPLES - an ordered set of different type elements.IMMUTABLE TYPES. ITERABLE OBJ.

from unicodedata import name


names = ('Roger', 'Syd', 'Indi')

names[0]  # Roger
names[-1]  # Indi
names[0:2]  # Roger, Syd
len(names)  # 2
sorted(names)
names.index('Roger')  # 0

if 'Roger' in names:  # True
    print('True')

newTuple = names + ('Elka', 'Ema')
