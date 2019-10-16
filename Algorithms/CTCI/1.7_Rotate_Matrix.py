def rotate_matrix(matrix):
    N = len(matrix)
    
    for x in range(N//2):
        for y in range(x, N-1-x):
            temp = matrix[x][y]
            matrix[x][y] = matrix[y][N-x-1]
            matrix[y][N-x-1] = matrix[N-x-1][N-y-1]
            matrix[N-x-1][N-y-1] = matrix[N-y-1][x]
            matrix[N-y-1][x] = temp

    return matrix

def printMatrix(arr): 
    for i in range(len(arr)): 
        for j in range(len(arr)): 
            print(str(arr[i][j]), end =" ") 
        print()


arr = [ [10, 11, 12, 13], 
        [14, 15, 16, 17], 
        [18, 19, 20, 21], 
        [22, 23, 24, 25]]

printMatrix(arr) 
arr2 = rotate_matrix(arr)
print("*"*30)
printMatrix(arr2) 
