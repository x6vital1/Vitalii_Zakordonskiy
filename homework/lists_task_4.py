input_string = input("Введите последовательность целых чисел разделенных проблеом: ")
numbers = list(map(int, input_string.split()))

last_two = numbers[-2:]

numbers = numbers[:-2]

numbers = last_two + numbers

print("Список с двумя послденими элементами вначале:")
print(numbers)