IOEA

1 - INPUT


2 - OUTPUT


3 - EDGE CASES
	1. Input is Null
	2. Input has length of 1, 2 

4 - ASSUMPTION  


5 - BIG O 

    Describes the space/time complexity of an algorithm. Measures how the algorithm grows relative to the size of its input.

    - O(n^2): Quadratic 
	-> Algorithm whose performance is 
	-> Often found when we iterate over the input using nested loops
	-> Card Deck Example:
		- If we pick the first card, and remove all cards with that same number.
		- We'd have to search through the entire deck for each card in the deck. 
		- Then we'd select the second card, and search the entire deck for each value. 

    - O(nlogn)
	-> Commonly found in comparison based sorting algorithms

    - O(n): Linear
	-> Complexity grows in direct proportion to the size of the input data.
	-> 
	-> Card Deck Example:
		- We want to select a specific card, let's say 10 of Spade. 
		- We need to look through every card until we find that card.
		- Sure, it's possible that its the first card in the deck, but that's highly unlikely.
		-> Big O measures the worst case scenario. So if it was the last card of the deck, it would take O(n)

    - O(logn): Logarithmic 
	-> Common case is when we are able to shrink the input size in half with every iteration using binary search.
	-> Card Deck Example:
		- We have a sorted deck of cards and asked to find a 10
		- Start by halving the deck. 
		- We see the card is a 7. 10 is higher than 7, so we know we only have to search the higher half.
		- Half again, we  get a Queen, a queen is higher than 10. We only search the higher half
	-> Effectively discard half of the search space with every iteration.

    - O(1): Constant 
	-> Size of the input does not effect run time.
	-> Algorithm will execute in the same time (or space) regardless if the input size is 5, 5,000, or 5 million.
	-> Card Deck Example:
		- If we have a trivial function that draws the very top card, doesn't matter if we have one deck or ten thousand decks. 
	-> 


References:
Card Example: https://medium.com/@ariel.salem1989/an-easy-to-use-guide-to-big-o-time-complexity-5dcf4be8a444