def process_values(var_1, var_2):
    if isinstance(var_1, int) and isinstance(var_2, str):
        result = str(var_1) + var_2
    else:
        try:
            var_1 = int(var_1)
            var_2 = int(var_2)
            result = var_1 + var_2
        except ValueError:
            result = str(var_1) + var_2

    return result

if __name__ == "__main__":
    var_1 = input("Введите первое значение: ")
    var_2 = input("Введите второе значение: ")

    result = process_values(var_1, var_2)
    print("Результат:", result)
