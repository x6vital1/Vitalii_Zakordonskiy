input_string = input("Введите спико чисел разделенных пробелом: ")
numbers = list(map(int, input_string.split()))

element_count = {}
for num in numbers:
    if num in element_count:
        element_count[num] += 1
    else:
        element_count[num] = 1

unique_elements = [num for num, count in element_count.items() if count == 1]
print("Элементы которые встречаются лишь один раз:", unique_elements)
