rows, cols = map(int, input().split())

matrix = []
for i in range(rows):
    a = []
    for j in range(cols):
        a.append(int(input()))
    matrix.append(a)

b = [[0 for x in range(cols)] for y in range(rows)]
for i in range(cols):
    for j in range(rows):
        B[i][j]=matrix[j][i]
print(matrix)