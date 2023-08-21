# input_string1 = input("Введите превый список чисел разделяя проблемами: ")
# list1 = list(map(int, input_string1.split()))
#
# input_string2 = input("Введите воторй список чисек: ")
# list2 = list(map(int, input_string2.split()))
#
# number_count = {}
# for num in list1:
#     number_count[num] = list2.count(num)
#
# print("{:<10} {:<10}".format("Число", "Кол-во"))
# print("="*25)
# for num, count in number_count.items():
#     print("{:<10} {:<10}".format(num, count))

input_string1 = input("Введите превый список чисел разделяя проблемами: ")
list1 = list(map(int, input_string1.split()))

input_string2 = input("Введите воторй список чисек: ")
list2 = list(map(int, input_string2.split()))

number_count1 = {}
for num in list1:
    number_count1[num] = list2.count(num)

number_count2 = {}
for num in list2:
    number_count2[num] = list1.count(num)

print("{:<10} {:<10} {:<10}".format("Число", "Кол-во в списке 1", "Кол-во в списке 2"))
print("="*40)
for num in sorted(set(list1 + list2)):
    count1 = number_count1.get(num, 0)
    count2 = number_count2.get(num, 0)
    print("{:<10} {:<10} {:<10}".format(num, count1, count2))