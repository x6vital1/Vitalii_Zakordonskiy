import random


def is_prime(num):
    if num <= 1:
        return False
    if num <= 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    return True


def generate_primes_in_range(N, Z):
    primes = [num for num in range(N, Z + 1) if is_prime(num)]
    return primes


N = random.randint(1, 100)
Z = random.randint(N, 200)

print(f"Диапазон от {N} до {Z} простые числа:")
prime_numbers = generate_primes_in_range(N, Z)
print(' '.join(map(str, prime_numbers)))
