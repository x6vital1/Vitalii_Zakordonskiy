import random

random_dict = {}

for i in range (16):
    key = random.randint(1, 10)
    value = key**3
    random_dict[key] = value

print(random_dict)