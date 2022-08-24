# SETS - unordered and mutable data type. Unique elements.

set1 = {'Potter', 'Ronald', 'Hermione'}
set2 = {'Potter', 'Rubeus '}

# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# SET METHODS

set1.add('Hermione')  # Potter, Ronald, Hermione
set1.update(['Luna ', 'Neville'])  # Potter, Ronald, Hermione, Luna, Neville
set1.remove('Luna ')  # If does not exist -> error
set1.discard('Neville')  # Does not give an error
set1.clear()
set1.pop()  # Delete and return random element

# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# OPERATIONS ON SETS

len(set1)  # 3
'Roger' in set1  # True
intersect = set1 & set2  # Potter OR set1.intersection(set2)
mod = set1 | set2  # Potter, Ronald, Hermione, Rubeus OR set1.union(set2)
mod = set1 - set2  # Ronald, Hermione
mod = set1 ^ set2  # Ronald, Hermione, Rubeus


# FROZENSET - frozenset() becomes an immutable data type as a tuple
frozenset(set1)

# Delete all dublicate records from list
set(['Potter', 'Ronald', 'Ronald', 'Hermione', 'Hermione'])

# Can convert into list type
list(set1)
