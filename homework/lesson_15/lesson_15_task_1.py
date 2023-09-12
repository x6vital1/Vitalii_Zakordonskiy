with open("test.txt", 'a', encoding='utf-8') as file:
    while True:
        data_to_write = input("Введите данные дял записи: ")
        if not data_to_write:
            break
        file.write(data_to_write + '\n')

print("Запись завершена!")
