def rotate(matrix):
    n = int(input())

    for i in range(n):
        matrix.append(list(map(int,input().split())))

    for i in range(n):
        for j in range(i,n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        for row in matrix:
            row.reverse()

        for row in matrix:
            print(*row)

matrix= []
rotate(matrix)