# Slice
A reference sheet for Python slice operations.

## Slicing 
Slicing allows us to access portions of strings, lists, and tuples.

Slicing works by defining a start and stop value for the slice. 

```
a[start:stop]        # items from start through stop-1
a[start:]              # items from start through end 
a[:stop]              # items from beginning through stop-1
a[:]                    # items from beginning through the end 
```
The stop value represents the first value that is NOT in the selected slice. 

- Leaving the stop value empty will slice from the start value to the end.
- Leaving the start value empty will slice from the beginning to the stop value - 1.
- Leaving both stop and start values empty will return a copy of the entire object

## A slicing example
Imagine we define a variable 'example' to be equal to the string 'PYTHON'

```
>>> example = 'PYTHON'
```

We will run a few indexing and slicing operations on our example string.

```
>>> example[0] 
['P']
>>> example[3] 
['H']
>>> example[0:3]
['P', 'Y', 'T']
``` 
The slice operation did NOT include the value at the third index. 

Remember, the slice operation returns items from start through stop - 1. 

In this case, the start value was 0 and the stop value was 3. 
Thus, the slice operation returned items from index 0 through 2.

The index and slicing positions are depicted below.

```
  0   1   2   3   4   5      <------- Index Positions 
+---+---+---+---+---+---+
| P | Y | T | H | O | N |
+---+---+---+---+---+---+
0   1   2   3   4   5   6    <------- Slicing Positions 
```
Notice that slicing positions point in between characters while index positions point to the actual value.

Finally, slicing will not modify the original object. Slicing will return a new object. 

```
>>> arr = ['a', 'b', 'c', 'd']
>>> slice = arr[0:2]
>>> print(slice)
['a', 'b']
>>> print(arr)
['a', 'b', 'c', 'd']
```