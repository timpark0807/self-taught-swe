# Dictionary
Unordered collection of data. 

Holds key:value pairs

Keys must be immutable (string, integer, tuples)

## Initialize
```
dictionary = {}
```

## Access
```
>>> dictionary['Denver']
'Broncos'
>>> dictionary['Test']
KeyError: 'Test'
```

### Add
dict[key] = value
```
>>> dictionary['Denver'] = 'Broncos'
>>> dictionary
{'Denver' : 'Broncos'}

>>> dictionary['Seattle'] = 'Seahawks'
>>> dictionary['Carolina'] = 'Panthers'
>>> dictionary
{'Denver': 'Broncos', 'Seattle': 'Seahawks', 'Carolina': 'Panthers'}
```
### Update
```
>>> dictionary['Seattle'] = 'Mariners
>>> dictionary
{'Denver': 'Broncos', 'Seattle': 'Mariners', 'Carolina': 'Panthers'}
```
## Removal
Removes a key and it's value
```
>>> del dictionary['Seattle']
>>> dictionary
{'Denver':'Broncos', 'Carolina': 'Panthers'}
```

## Test 
Check if a __key__ exists 
```
>>> 'Carolina' in dictionary
True
>>> 'Seattle' in dictionary
False
```

## Built-in Operators

__Clear__
```
>>> d.clear()
>>> d
{}
```

__Get__

Provides a convenient way of getting the value of a key from a dictionary without checking ahead of time whether the key exists, and without raising an error.
Returns 'None' if key is not found in the dictionary.
```
# dictionary.get(<key>)
>>> print(d.get('Seattle'))
None
>>> print(d.get('Carolina'))
'Panthers'
```

__Items__

Returns a list of key-value pairs in a dictionary
```
>>> d.items()
```

__Keys__

Returns a list of keys in a dictionary.
```
>>> d.keys()
```

__Values__

Returns a list of values in a dictionary
```
>>> d.values()
```

__Pop__

Removes a key from a dictionary, if it is present, and returns its value.
```
d.pop(<key>)
```

__Update__

Merges a dictionary with another dictionary or with an iterable of key-value pairs
```
```

## Iteration
We can use dictionary.items(), dictionary.keys(), and dictionary.values() to iterate 
```
for key in d:
    print d[key]

'Broncos'
'Panthers'
```


## Properties of Dictionary Keys
1. No Duplicates
2.  Must be immutable
