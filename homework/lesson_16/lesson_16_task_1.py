import random


def matrix_generator():
    matrix = []
    m = int(input("Введтие число M для генирации матрици: "))
    for i in range(m):
        row = []
        for j in range(m):
            row.append(random.randint(1, 50))
        matrix.append(row)
    print("Матрица до сортировки:")
    for row in matrix:
        for num in row:
            print(f"{num:4}", end=" ")
        print()


matrix_generator()
