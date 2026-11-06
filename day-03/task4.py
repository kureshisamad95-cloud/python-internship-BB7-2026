matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
transpose = [[matrix[j][i] for j in range(3)] for i in range(3)]

print("Original matrix:")
for row in matrix:
    print(row)
    
    print("Transpose matrix:")
    for row in transpose:
        print(row)