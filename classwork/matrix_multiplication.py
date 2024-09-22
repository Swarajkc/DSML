#Doing Matrix Multiplication by taking the input from user
def matrix_multiply(A, B):
    rows_A = len(A)
    cols_A = len(A[0]) if rows_A > 0 else 0
    rows_B = len(B)
    cols_B = len(B[0]) if rows_B > 0 else 0

    result = [[0] * cols_B for _ in range(rows_A)]

    for i in range(rows_A):
        for j in range(cols_B):
            for k in range(cols_A):
                result[i][j] += A[i][k] * B[k][j]

    return result

i = int(input("Enter the number of rows for matrix 1: "))
j = int(input("Enter the number of columns for matrix 1: "))
k = int(input("Enter the number of rows for matrix 2: "))
l = int(input("Enter the number of columns for matrix 2: "))

if j == k:
    matrix1 = []
    matrix2 = []
    
    print("Enter the elements of matrix 1 (row-wise):")
    for row in range(i):
        matrix1.append([int(x) for x in input().split()])
    
    print("Enter the elements of matrix 2 (row-wise):")
    for row in range(k):
        matrix2.append([int(x) for x in input().split()])

    result = matrix_multiply(matrix1, matrix2)

    print("Result of matrix multiplication:")
    for row in result:
        print(row)
else:
    print("Invalid input: Number of columns in matrix 1 must equal number of rows in matrix 2.")
