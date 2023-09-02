my_func = lambda x, y=2: x ** y

input_list_1 = [2, 3, 4, 5]
result_1 = list(map(my_func, input_list_1))
print("Результат примерп 1:", result_1)

input_list_2_x = [1, 2, 3]
input_list_2_y = [2, 3, 4]
result_2 = list(map(my_func, input_list_2_x, input_list_2_y))
print("Результат примера 2:", result_2)
