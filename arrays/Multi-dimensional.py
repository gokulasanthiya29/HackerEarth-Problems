rows, cols = input().split()

matrix = []

for i in range(int(rows)):
    matrix[i] = input().split()

for i in range(int(cols)):
    for j in range(int(rows)):
        print(matrix[j][i], sep="", end=" ")
    print('\n')
