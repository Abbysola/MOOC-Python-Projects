# Write your solution here
def transpose(matrix: list):
    transposed_matrix = []
    for i in range(len(matrix)):
        transposed_row = []
        for j in range(len(matrix[i])):
            transposed_row.append(matrix[i][j])
        transposed_matrix.append(transposed_row)
    matrix = transposed_matrix
    

 #[1,4,7],[2,5,8],[3,6,9]
    transpose([[1,2],[2,1]])