# DICTIONARIES - key:value pairs. MUTABLE AND ITERABLE TYPE.
# key: can be only immutable value (str, number, tuple).

dog = {'name': 'Roger', 'age': 5}

dog['name']  # Roger
dog['age'] = 7
dog['age']  # 7

len(dog)  # 2

dog['favorite_food'] = 'Meat'

dog.get('name', 'Default')  # Roger. If key does't exist return default value
dog.pop('name')
dog.popitem()  # Delete and return the last pair in dict
dog.values()  # ['Roger', 5] -> list(dog.values() )
dog.items()  # ('name', 'Roger'), ('age', 5)
dog.keys()  # ['name', 'age'] -> list(dog.keys())

dic = {'x': 2}  # {'x': 2, 'y': 3, 'z': 0}
dic.update([('y', 3), ('z', 0)])

dic2 = {'w': 5}  # {'x': 2, 'y': 3, 'z': 0, 'w': 5}
dic.update(dic2)


del dog['favorite_food']

dogCopy = dog.copy()

if 'name' in dog:  # Roger
    print(dog['name'])
