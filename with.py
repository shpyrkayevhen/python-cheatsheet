# Automatically file.close()
filename = 'path_to_file'

with open(filename, 'r') as file:
    content = file.read()
    print(content)
