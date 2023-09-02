import random


def my_func(numbers, target):
    seen_numbers = set()

    for num in numbers:
        complement = target - num
        if complement in seen_numbers:
            return True
        seen_numbers.add(num)

    return False


user_target1 = int(input("Введите число для поиска(1 Список): "))
user_target2 = int(input("Введите число для поиска(2 Список): "))

numbers_1 = []
numbers_2 = []

for i in range(5):
    numbers_1.append(random.randint(1, 10))
    numbers_2.append(random.randint(1, 10))

print(f"Список 1: {numbers_1}, Список 2: {numbers_2}")
print(my_func(numbers_1, user_target1))
print(my_func(numbers_2, user_target2))
