import random

pair_numbers = 0
unpaired_numbers = 0
random_numbers = [random.randint(1, 10) for i in range(15)]

for num in random_numbers:
    if num % 2 == 0:
        pair_numbers += num
    else:
        unpaired_numbers += num

print(random_numbers)

if pair_numbers < unpaired_numbers:
    print("Yes")
else:
    print("No")
