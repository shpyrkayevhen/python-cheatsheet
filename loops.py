# LOOPS

# -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# WHILE LOOP

# conditions = True

# while conditions == True:
#     print('The condition is True')

count = 0

while count < 10:
    count += 1
    print(f'Attempt № {count}')

# -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# FOR LOOP

items = ['Potter', 'Ronald', 'Hermione', 'Neville', 'Luna ']

# For value
for item in items:
    print(item)

# For index
for item in range(len(items)):
    print(items[item])

# Get index and value
for intex, value in enumerate(items):
    print(intex, value)


items = [1, 2, 3, 4]

# Use continue
for item in items:
    if item == 2:
        continue
    print(item)  # 1, 3, 4

# Use break
for item in items:
    if item == 3:
        continue
    print(item)  # 1, 2

# -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# NESTED LOOPS
items = [['Potter', 'Ronald'], ['Hermione', 'Neville', 'Luna ']]

for i in range(len(items)):
    for j in range(len(items[i])):
        print(items[i][j])
