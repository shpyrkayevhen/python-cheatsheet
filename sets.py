# SETS - unordered and mutable data type. Unique elements.

set1 = {'Roger', 'Syd', 'Indi'}
set2 = {'Roger', 'Oliver'}

# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# SET METHODS

set1.add('Indi')  # Roger, Syd, Indi
set1.update(['Oliver', 'Barbur'])  # Roger, Syd, Indi, Barbur, Oliver
set1.remove('Oliver')  # If does not exist -> error
set1.discard('Barbur')  # Does not give an error
# set1.clear()
# set1.pop()  # Delete and return random element

# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# OPERATIONS ON SETS

len(set1)  # 3
'Roger' in set1  # True
intersect = set1 & set2  # Roger OR set1.intersection(set2)
mod = set1 | set2  # Roger, Syd, Oliver, Indi OR set1.union(set2)
mod = set1 - set2  # Syd, Indi
mod = set1 ^ set2  # 'Indi', 'Oliver', 'Syd'


# FROZENSET - frozenset() becomes an immutable data type as a tuple
frozenset(set1)

# Delete all dublicate records from list
set(['Roger', 'Roger', 'Adam', 'Indi'])  # Roger, Adam, Indi

# Can convert into list type
list(set1)
