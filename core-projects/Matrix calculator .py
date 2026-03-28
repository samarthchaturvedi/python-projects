# Matrix Calculator with User Input

def input_matrix(rows, cols):
    matrix = []
    print("Enter matrix values row-wise:")
    for i in range(rows):
        row = list(map(int, input().split()))
        matrix.append(row)
    return matrix

def display(matrix):
    for row in matrix:
        print(row)

# Input size
r = int(input("Enter rows: "))
c = int(input("Enter cols: "))

print("Matrix A:")
A = input_matrix(r, c)

print("Matrix B:")
B = input_matrix(r, c)

print("\n1.Add 2.Subtract 3.Multiply")
choice = input("Choose operation: ")

if choice == '1':
    result = [[A[i][j] + B[i][j] for j in range(c)] for i in range(r)]

elif choice == '2':
    result = [[A[i][j] - B[i][j] for j in range(c)] for i in range(r)]

elif choice == '3':
    result = [[0]*c for _ in range(r)]
    for i in range(r):
        for j in range(c):
            for k in range(c):
                result[i][j] += A[i][k] * B[k][j]

print("\nResult:")
display(result)