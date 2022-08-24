# LIST - an ordered set of different type elements. ITERABLE AND MUTABLE OBJ

items = ['Roger', 'indi', 'Syd']

items[0]  # Roger
items[-1]  # Syd
items[0] = 'Martin'  # ['Martin', 'Indi', 'Syd']
print(items[0:2])  # ['Roger', 'Indi']
len(items)  # 3
sorted(items)
items += ['Oliver']
items[0:3] = ['Test1', 'Test2', 'Test3']
itemscopy = items[:]  # Also we can do deep copy or sorted function

'Roger' in items  # False


# LIST METHODS
items.append('Barbur')
items.extend(['Judah', 'Bob'])
items.insert(2, 'Test')
items.pop()            # delete and return last intem
items.pop(3)           # delete and return item with index [3]
items.clear()          # clear all list
items.remove('Barbur')
items.sort(reverse=False, key=lambda x: x.title())
items.index('Roger')  # 0
