n = int(input("Введите размер матрицы N: "))

matrix = []

for i in range(n):
    row = []
    for j in range(n):
        if i % 2 == 0:
            row.append(-n + j)
        else:
            row.append(i + 1)
    matrix.append(row)

for row in matrix:
    for num in row:
        print(f"{num:4}", end=" ")
    print()
