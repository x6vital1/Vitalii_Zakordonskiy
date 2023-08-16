import random

print("Загадайте число от 1 до 100")

lower_bound = 0
upper_bound = 100
steps = 0

while True:
    number = random.randint(lower_bound, upper_bound)
    response = input(f"Это число {number}? Выберите 'больше', 'меньше' или 'да': ").lower()

    steps += 1

    if response == 'да':
        print(f"Программа угадала число {number} за {steps} шагов.")
        break
    elif response == 'больше':
        lower_bound = number + 1
    elif response == 'меньше':
        upper_bound = number - 1
    else:
        print("Введите 'больше', 'меньше' или 'да'.")