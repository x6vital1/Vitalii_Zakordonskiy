import random


def matrix_generator(m):
    return [[random.randint(1, 50) for _ in range(m)] for _ in range(m)]


def sort_matrix(matrix):
    column_sums = [sum(column) for column in zip(*matrix)]
    sorted_indices = sorted(range(len(column_sums)), key=lambda i: column_sums[i])
    sorted_matrix = [[row[i] for i in sorted_indices] for row in matrix]

    for i in range(len(sorted_matrix[0])):
        if i % 2 == 0:
            column = [sorted_matrix[j][i] for j in range(len(sorted_matrix))]
            column.sort(reverse=True)
            for j in range(len(sorted_matrix)):
                sorted_matrix[j][i] = column[j]
        else:
            column = [sorted_matrix[j][i] for j in range(len(sorted_matrix))]
            column.sort()
            for j in range(len(sorted_matrix)):
                sorted_matrix[j][i] = column[j]

    return sorted_matrix


def print_matrix(matrix):
    for row in matrix:
        for element in row:
            print(f'{element:2}', end=' ')
        print()

    column_sums = [sum(column) for column in zip(*matrix)]
    print("\nСуммы столбцов:", end=' ')
    for sum_value in column_sums:
        print(sum_value, end=' ')
    print()


if __name__ == "__main__":
    try:
        m = int(input("Введите размер матрици (M > 5): "))
        if m <= 5:
            print("Значение М должно быть больше 5.")
        else:
            matrix = matrix_generator(m)
            sorted_matrix = sort_matrix(matrix)
            print("Исходная матрица:")
            print_matrix(matrix)
            print("\nОтсортированная матрица:")
            print_matrix(sorted_matrix)
    except ValueError:
        print("Введено неверное значение для M.")
