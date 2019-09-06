# Heap
Tree representation of an array. 

## Properties
A Heap must be a complete binary tree 

- All levels are full, except possibly the last with all nodes being left most as possible.
- Allows us to implement a heap using an array

# Max vs. Min
Max Heap: Key of the parent node is greater than its children 

Min Heap: Key of the parent node is less than its children

# Height
Height = log2(n + 1) - 1

where n is equal to the number of nodes in the heap

# Parent and child relationship
N = Index of the current item

Parent of N = N // 2

Left Child of N = (N * 2)

Right Child of N = (N * 2) + 1

```
 0  1  2   3   4   5   6   7
[0, 5, 10, 15, 20, 25, 30, 35] 

When 5 is the root node, N = 1.
Left Child = (N * 2) = (1 * 2) = 2   
Right Child = (N * 2) + 1 = (1 * 2) + 1 = 3   

      5 
    /   \
   10   15 

When 10 is the root node, N = 2
Parent Node = (N // 2) = (2 // 2) = 1 
Left Child = (2 * 2) = 4
Right Child = (2 * 2) + 1 = 5

    	     5 
 	   /  \
	  10   15 
         /  \
        20   25

When 15 is the root node, N = 3. 
Parent Node = (N // 2) = ( 3 // 2 ) = 1 
Left Child = (N * 2) = (3 * 2) = 6
Right Child = (N * 2) + 1 = (3 * 2) + 1 = 7

    	       5 
 	   /       \
	  10        15 
         /  \      /  \ 
        20   25   30   35 
```

## Operations
build_max_heap
Produces a max heap from an unordered array.

We go from len(arr//2) to 1 because everything greater than len(arr//2) are leaves, which are good. 

Because tree is complete, any nodes past the halfway point will be leaves and therefore have no children.
```
for index in reversed(range(1, len(arr) // 2)):
    min_heapify(index)
```

2. min_heapify
In order to build_min_heapify, we must perform min_heapify.
```
Compare the value at the parent index to the value at the left and right child.
Swap smallest value into parent index position. 
```

3. 










