import random
from colour_for_lesson import mcolour as mc


def random_chess_piece():
    """
    Функция для случайной расстановки шахмат.
    :return: K - Король, Q - Королева, R - Ладья, N - Конь, B - Слон, P - Пешка
    """
    pieces = ['K', 'Q', 'R', 'N', 'B', 'P']
    return random.choice(pieces)


def generate_chess_board():
    """
    Генерирует шахматную доску.
    :return: шахматная доска 8*8
    """
    board = [[' ' for _ in range(8)] for _ in range(8)]

    for _ in range(5):
        while True:
            row = random.randint(0, 7)
            col = random.randint(0, 7)
            if board[row][col] == ' ':
                board[row][col] = random_chess_piece()
                break

    return board


def print_chess_board(board):
    """

    :param board: передача матрици шахматной доски.
    :return: Вывод шахматной доски 8*8
    """
    print(mc.universal_text_stile("   a  b  c  d  e  f  g  h", "red"))
    for i in range(8):
        print(mc.universal_text_stile(8 - i, "red"), end=" ")
        for j in range(8):
            if (i + j) % 2 == 0:
                print("\033[47m", end="")
            else:
                print("\033[40m", end="")

            print(" " + board[i][j] + " ", end="")
            print("\033[0m", end="")

        print(mc.universal_text_stile(" " + str(8 - i), "red"))
    print(mc.universal_text_stile("   a  b  c  d  e  f  g  h", "red"))


if __name__ == "__main__":
    chess_board = generate_chess_board()
    print_chess_board(chess_board)
