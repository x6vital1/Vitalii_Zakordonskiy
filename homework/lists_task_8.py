n = int(input("Кол-во рядков: "))
m = int(input("Кол-во столбиков
chessboard = [['.' if (i+j) % 2 == 0 else '*' for j in range(m)] for i in range(n)]


for row in chessboard:
    print(' '.join(row))
