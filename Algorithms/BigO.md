# Big O
Describes the performance or complexity of an algorithm. 
Specifically, Big O gives the upper limit, or worst case scenario, for how long or how much space an algorithm could take.  

## What is an Algorithm?
An algorithm is a set of instructions to find the solution to a problem. 

## Benefits of Big O
- Ignores differences in hardware, programming language, and other external factors that effect run time. 
- Allows us to explain how algorithms behave as the input grows larger

## Asymptotic behavior
- How a function behaves as n approaches infinity
- Focus on only the largest growing term
- Example: O(n^2 + 100n) is reduced to O(n^2) because as n grows larger, 100n becomes less and less important. 

## Common Time Complexities
- O(1) = Constant 
- O(n) = Linear 
- O(n^2) = Quadratic 
- O(logn) = Logarithmic 

### O(n^2)
A loop within a loop is O(n^2)
