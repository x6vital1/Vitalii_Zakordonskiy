import random

n = int(input("Введите размер матрицы N: "))
matrix = []

for i in range(n):
    row = []
    for j in range(n):
        random_number = random.randint(1, 100)
        row.append(random_number)
    matrix.append(row)

main_diagonal_sum = sum(matrix[i][i] for i in range(n))
secondary_diagonal_sum = sum(matrix[i][n - i - 1] for i in range(n))
last_column_sum = sum(matrix[i][-1] for i in range(n))
column_widths = [max(len(str(matrix[i][j])) for i in range(n)) for j in range(n)]

for row in matrix:
    for j in range(n):
        print(f"{row[j]:{column_widths[j]}}", end=" ")
    print()

print(f"Сумма главной диагонали: {main_diagonal_sum}")
print(f"Сумма побочной диагонали: {secondary_diagonal_sum}")
print(f"Сумма последнего столбца: {last_column_sum}")
