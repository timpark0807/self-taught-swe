def rotate_matrix(matrix):
    
    N = len(matrix)
    
    for x in range(N//2):
        for y in range(x, N-x-1):
            
            temp = matrix[x][y]
            
            matrix[x][y] = matrix[N-y-1][x]
            matrix[N-y-1][x] = matrix[N-x-1][N-y-1]
            matrix[N-x-1][N-y-1] = matrix[y][N-x-1]
            matrix[y][N-x-1] = temp

    return matrix



matrix = [
            [1,2,3,1],
            [4,5,6,4],
            [7,8,9,9],
            [3,6,7,8]
            ]

output = rotate_matrix(matrix)

for line in output:
    print(line)
