def zero_matrix(matrix):
    stored = []
    y = len(matrix)
    x = len(matrix[0])
    
    # identify zeroes
    for row in range(y):
        for col in range(x):
            if matrix[row][col] == 0:
                stored.append((row, col))

    for item in stored:
        row, col = item[0], item[1]

        # Zero out row
        for index in range(x):
            matrix[row][index] = 0

        # Zero out column
        for index in range(y):
            matrix[index][col] = 0 

    return matrix

def print_matrix(matrix):
    for row in matrix:
        print(' '.join(map(str,row)))
  
matrix = [[1, 1, 1, 1],
          [1, 1, 1, 1],
          [0, 1, 1, 1],
          [1, 1, 1, 1],
          [1, 1, 1, 1],
          [1, 1, 1, 0],
          [1, 1, 1, 1]]

print('Original Matrix')
print_matrix(matrix)
print('')
print('Zero Matrix')
zero_matrix = zero_matrix(matrix)
print_matrix(zero_matrix)


