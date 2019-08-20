# Heap
Tree representation of an array. 

## Properties
A Heap must be a complete binary tree 
    - All levels are full, except possibly the last with all nodes being left most as possible.
    - Allows us to implement a heap using an array

# Max vs. Min
Max Heap: Parent node is greater than its children 

Min Heap: Parent node is less  than its children

# Height
Height = log 2 (n + 1) - 1

where n is equal to the number of nodes in the heap

# Parent and child relationship
N = Index of the current item

Parent of N = N // 2

Left Child of N = (N * 2)

Right Child of N = (N * 2) + 1

```
 0  1  2  3  4  5  
[0, 5, 10, 15, 20, 25] 

When 5 is the root node, N = 1.
Left Child = (N * 2) = (1 * 2) = 2   
Right Child = (N * 2) + 1 = (1 * 2) + 1 = 3   

      5 
    /   \
   10   15 

When 2 is the root node, N = 2
Parent Node = (N // 2) = (2 / 2) = 1 
Left Child = (2 * 2) = 4
Right Child = (2 * 2) + 1 = 5

    	     5 
 	   /   \
	  10   15 
         /  \
        20   25
```