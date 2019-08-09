# Initiliaze a dictionary with curly braces
d = {}

# Add items to the dictionary by defining a key and a value
# dictionary[key] = value
d['Arizona'] = 'Cardinals'
d['Los Angeles'] = 'Chargers'
d['San Francisco'] = '49ers'
d['Seattle'] = 'Seahawks'

# Update an item in the dictionary by overwriting the original key
d['Los Angeles'] = 'Rams'

# Access dictionary value using its key -> dictionary[key]
print('Access:')
print(d['Seattle'])

# Iteration
# Iterate over keys
print('*' * 30)
print('Iteration over keys:')
for i in d.keys():
    print(i)

# Iterate over values
print('*' * 30)
print('Iteration over values:')
for i in d.values():
    print(i)

# Iterate over key, value pairs
print('*' * 30)
print('Iteration over key, value pairs:')
for i, j in d.items():
    print(i, j)

# Delete values from the dictionary using del
print('*' * 30)
print('Delete values')
del d['Seattle']
print(d)

# Pop allows us to define a value in case of a key error
print('*' * 30)
a = d.pop('Seattle', 'N/A')
print(a)
print(d)
