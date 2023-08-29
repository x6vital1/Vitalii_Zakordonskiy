import random

random_dict = {}
result = 1

for i in range(21):
    key = f'key_{i}'
    value = random.randint(1, 10)
    random_dict[key] = value

for value in random_dict.values():
    result *= value

print(random_dict)
print(f"Результат умножения: {result}")