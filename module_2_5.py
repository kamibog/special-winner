def get_matrix(n, m, value):
    matrix = []
    for i in range(n):
        matrix.append([])
        for j in range(m):
            matrix[i].append(value)
    print(matrix)
    return matrix


n = int(input(':'))
m = int(input(':'))
value = input(f':')
print('' * m)
matrix = get_matrix(n, m, value)
if n <= 0:
    print("0:", n)
elif m <= 0:
    print("0:", m)
else:
    print("Матрица:")
    for i in matrix:
        print(*i)
        result1 = get_matrix(5, 6, 8)
        result2 = get_matrix(12, 13, 14)
        result3 = get_matrix(9, 1, 15)
        print(result1)
        print(result2)
        print(result3)
