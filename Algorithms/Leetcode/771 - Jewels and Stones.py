def numJewelsInStones(J, S):
    count = 0 
    for stone in S:
        if stone in J:
            count += 1
    return count
    
  

J = "aA"
S = "aAAbbbb"
print(numJewelsInStones(J, S))
