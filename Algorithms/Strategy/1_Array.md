# Leetcode Strategy : Arrays

0. Clarify
	1. Are we modifying the array in place?
	2. What are we returning? The array, index, value, nothing?
	3. Does the order of the values inside the array matter? 
		- No? Let's consider sorting.
	4. What if the array is empty?
	5. If string: How should we handle Upper/Lower, spaces, and punctuation?

1. Derive the Brute Force solution
	- Often times this involves using nested for loops giving us O(n^2)

2. Assess a time/space tradeoff	
	1. Can we make the algorithm faster by introducing an auxiliary data structure?
		- Think Hash tables
	2. Can we make the algorithm use one pass?
		- Think 2 Pointers

3. Test/Edge cases
	1. Test a normal case
	2. Test an empty array
	3. Test an array length 1 

3. Common Techniques
	1. Divide problems into subproblems


As an example, I will be going over the strategy used to solve the Two Sum array problem.

```
Input: numbers = [2,7,11,15], target = 9
Output: [1,2]
Explanation: The sum of 2 and 7 is 9. Therefore index1 = 1, index2 = 2.
```
## 0. Clarify
	- Algorithm does not need to be in place.
	- Returning 2 indicies as a list
	- Order does not matter
	- If array is empty, return None
	- If len(array) == 1, return None

## 1. Identify the brute force solution
	- Loop through each element x 
		- O(n)
	- Loop through array to check if there is a value that equals target - x
		- O(n) 
	- Time  :  O(n^2)
		- For each element O(n), we try to find its complement by looping through the rest of the array O(n). 
	- Space :  O(1)

## 2. Make a time/space tradeoff 
	- Is there a more efficient way to check if the complement exists?
		-> We can reduce the look up time from O(n) to O(1) by trading space for speed.
		-> A hash table looks up in O(1) time

## 3. Optimize
	- Use 2 iterations
		1. Add each element's value and index to the dictionary
		2. Check is each element's complement exists in the dictionary

	- Time   :   O(n)
		-> Traverse the list containing n elements, twice.

	- Space  :   O(n) 
		-> Hash Table reduces look up time to O(1) 
