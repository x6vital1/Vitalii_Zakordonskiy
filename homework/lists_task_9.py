input_string1 = input("Введите превый список чисел разделяя проблемами: ")
list1 = list(map(int, input_string1.split()))

input_string2 = input("Введите воторй список чисек: ")
list2 = list(map(int, input_string2.split()))

number_count = {}
for num in list1:
    number_count[num] = list2.count(num)

print("{:<10} {:<10}".format("Число", "Кол-во"))
print("="*25)
for num, count in number_count.items():
    print("{:<10} {:<10}".format(num, count))
