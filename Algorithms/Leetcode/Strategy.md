# Leetcode Strategy
In this example, I will be going over the strategy used to solve the Two Sum problem.

```

Input: numbers = [2,7,11,15], target = 9
Output: [1,2]
Explanation: The sum of 2 and 7 is 9. Therefore index1 = 1, index2 = 2.
```

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
		2. Check is each element's cmplement exists in the dictionary

	- Time   :   O(n)
		-> Traverse the list containing n elements, twice.

	- Space  :   O(n) 
		-> Hash Table reduces look up time to O(1) 
