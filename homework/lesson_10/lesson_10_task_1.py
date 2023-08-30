import random

my_list = []

for num in range(10):
    my_list.append(random.randint(1, 10))

unique_count = len(set(my_list))

print(f"Список случайных чисел: {my_list}")
print(f"Уникальных цифр: {unique_count}")
