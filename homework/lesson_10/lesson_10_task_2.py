import random

list_1 = []
list_2 = []

for num in range(10):
    list_1.append(random.randint(1, 10))
    list_2.append(random.randint(10, 20))

combined_set = set(list_1 + list_2)

print(f" Список 1: {list_1} \n Список 2: {list_2}")
print(f"Множество из объедененных двух списков: {combined_set}")
print(f"Уникальных цифр: {len(combined_set)}")
