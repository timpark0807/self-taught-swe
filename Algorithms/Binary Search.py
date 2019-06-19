# Binary Search

def binary_search(test_list, answer):
    # set low and high ranges
    low = 0
    high = len(test_list) - 1
    guess = 0

    # while guess is not equal to the answer
    while guess != answer:
        
        # Calculate our guess, the middle of low and high
        mid = (high + low) // 2
        guess = test_list[mid]
        
        # if guess is greater than the answer
        # we can eliminate everything greater than the guess
        # the new high is our guess
        if guess > answer:
            high = guess
            
        # if guess is lower than the answer
        # we can eliminate everything below the guess
        # the new low is our guess
        if guess < answer:
            low = guess

        
    # Once guess == answer, the while loop will break
    print('answer is:', guess)



binary_search(range(0,1000), 88)
