def sortedSquares(A):
    for i, num in enumerate(A):
        A[i] = num ** 2
    return sorted(A)




print(sortedSquares([-4,-1,0,3,10]))
