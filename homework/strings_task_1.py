string = input("Введите строку: ")
char = input("Введите символ для поиска: ")
count = 0
for i in string:
    if i == char:
        count += 1
print(f"Символ '{char}' встречается в строке - '{string}' {count} раз(а).")

# string = input("Введите строку: ")
# char = input("Введите символ для поиска: ")
#
# count = 0
# index = 0
#
# while index != -1:
#     index = string.find(char, index)
#     if index != -1:
#         count += 1
#         index += 1
#
# print(f"Символ '{char}' встречается в строке {count} раз(а).")