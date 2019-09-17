# Big O
Describes the performance or complexity of an algorithm. 
Specifically, Big O gives the upper limit, or worst case scenario, for how long or how much space an algorithm could take.  

## What is an Algorithm?
An algorithm is a set of instructions to find the solution to a problem. 

We need to choose the correct data structure for our algorith in order for the algorithm to be efficient.

## Benefits of Big O
- Ignores differences in hardware, programming language, and other external factors that effect run time. 
- Allows us to explain how algorithms behave as the input grows larger

## Asymptotic behavior
- How a function behaves as n approaches infinity
- Drop any constants
- Focus on only the largest growing term
- Example: O(2n^2 + 100n) is reduced to O(n^2) because as n grows larger, 100n becomes less and less important. 

## Calculating Complexity 
We will combine complexity class information about simple operations, into complexity class information about complex operations (composed from simple operations).

Thus, in order to determine the complexity class of executing a function, we must be able to analyze all operations/statements contained in the function. 

### Law of Addition 
We use the law of addition when operations are executed in sequence.
```
Big O of a Sequence = Time Complexity of Operation 1 + Time Complexity of Operation 2
```
An example function containing operation f and operation g is defined below.
```
def example(n):
    f()
    g()
```
We could describe the execution of example(n) as "do operation f and then do operation g." 

According to the Law of Addition, the big O of example(n) would look like...
```
O(example(n)) = O(f()) + O(g())
```
We can use the Law of Addition to further modify the statement above to below...
```
O(example(n))  = O(f()) + O(g())  =  O( f() + g() )
```
If both f() and g() require O(n) time, then plugging in O(n) time results in...
```
O(example(n))  = O(n) + O(n)  =  O( n + n ) = O(2n)
```
This is finally simplified to ```O(n)``` after we drop all constants. 

The runtime of our example function is ```O(n)```.

### Law of Multiplication
```
O(f(n)) * O(g(n)) = O( f(n) * g(n) )
```
We use the Law of Multiplication when we repeat an operation X, Y amount of times.
```
(time complexity of operation X) * Y amount of repeats
```
If we repeat an O(f(n)) process O(n) times, the resulting complexity is 
```
O(f(n)) * O(n) = O( f(n)*n ) 
```
Another example function is defined below.
```
def example(n):
    for i in range(n):
        f()
```
We can describe the execution of example(n), "do f(), n times".
```
O(f(n)) * O(n) = O( f(n)*n ) 
```
If O(f(n)) is n, and we run it n times,
```
O(n) * O(n) = O( n*n ) 
```
O(n^2)

### Summary
Compound statements are analyzed by composing complexity classes of their constituent statements.

For sequentials statements (such as if, else), the complexity classes are added.

For repeating statements (such as loops), the complexity classes are multiplied. 






## Common Time Complexities
- O(1) = Constant 
- O(n) = Linear 
- O(n^2) = Quadratic 
- O(logn) = Logarithmic 

## Constant Time
An algorithm has constant time when it is not dependent on the input data (n).
No matter the size of the input data, the running time will always be the same.
```
def get_first(data):
    return data[0]

>>> get_first([10, 20, 30])
10
```
It does not matter whether there are 1 or 1,000,000 elements in data. 
The function will only return the first value in data
We do not need to worry about input size

### Logarithmic Time
When the algorithm reduces the size of the input data in each step, it is logarithmic. 
When the number of elements in the problem space get halved each time, that is likely O(log n) run time
```
Input step on each step of binary search
N = 16
N = 8
N = 4
N = 2
N = 1
```

### Linear Time
When the run time increases linearly with the size of the input data.
```
def linear_search(data, value):
    for index in range(len(data)):
        if value == data[index]:
            return index

data = [1, 2, 9, 8, 3, 4, 7, 6, 5]
print(linear_search(data, 7))
```
As the size of data grows, the number of operations grow - linearly.


### Quadratic Time
When it needs to perform a linear time operation for each value in the input data
A loop within a loop is O(n^2)
Do this for each time you do that
Inner loop has O(N) iterations and it is called N times.

### Recursive runtime
O(branches ^ depth)
