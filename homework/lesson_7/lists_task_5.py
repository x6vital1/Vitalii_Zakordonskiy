input_string = input("Введите список чисел разделенных пробелом ")
numbers = list(map(int, input_string.split()))

positive_count = sum(1 for num in numbers if num > 0)

print("Кол-во положительных элементов:", positive_count)
