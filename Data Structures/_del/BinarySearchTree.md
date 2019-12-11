# Binary Search Tree

Heap is an array, visualized as a tree.
Binary tree is a tree, which has pointers.

Requires additional memory for pointers. 
- Parent
- Left Child
- Right Child

Ordering of key values for that all nodes X: 
- If Y is in the left subtree of X, Key(Y) <= Key(X)
- If Y is in the right subtree of X, Key(Y) >= Key(X)

This ordering is true for the entire subtree, where heaps ordering is only true for the parent and its children.

	  49
       /      \
      46       79
     /  \     /  \ 
    41       69   83
   

if h -> height of the tree, the insertion is O(h).

## Operations
Find 
Insert
Find Min - Keep going to left until you hit a leaf O(h)
Find Max - Keep going to right until you hit a leaf O(h)