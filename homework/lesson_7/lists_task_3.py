input_string = input("Введите список целых чисел разделенных пробелом: ")
numbers = list(map(int, input_string.split()))

min_index = numbers.index(min(numbers))
max_index = numbers.index(max(numbers))

numbers[min_index], numbers[max_index] = numbers[max_index], numbers[min_index]

print("Список после замены максимального и минимального значения:")
print(numbers)