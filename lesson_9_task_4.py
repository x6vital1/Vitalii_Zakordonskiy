import random

keys = []
values = []

for i in range(5):
    value = random.randint(1, 10)
    values.append(value)
    key = f"key_{i + 1}"
    keys.append(key)

my_dict = dict(zip(keys, values))
print(my_dict)
