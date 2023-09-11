def dict_handler(link_on_dict, key, default_value):
    """

    :param link_on_dict: .....
    :param key: .....
    :param default_value:.....
    :return:
    """
    try:
        value = link_on_dict[key]
    except KeyError:
        link_on_dict[key] = default_value
        value = default_value
    except TypeError:
        raise ValueError("Ключ не может быть переменным типом данных")
    finally:
        return value


# Приклад використання функції
my_dict = {'a': 1, 'b': 2}
result = dict_handler(my_dict, 'c', 4)
print(f"Новый словарь: {my_dict}")
print(f"Резултатат: {result}")
