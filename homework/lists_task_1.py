numbers = list(range(10, 251))

numbers = [num for num in numbers if num % 20 != 0]

print(numbers)