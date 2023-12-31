# Определение словаря 'colour', который сопоставляет названия цветов с кодами ANSI escape.
colour = {
    'red': '31m',
    'black': '30m',
    'green': '32m',
    'yellow': '33m',
    'blue': '34m',
    'purpure': '35m',
    'biruza': '36m',
    'white': '37m',
    'bg_red': '41m',  # Добавляем цвет фона к словарю
    'bg_black': '40m',  # Добавляем цвет фона к словарю
    'bg_green': '42m',  # Добавляем цвет фона к словарю
    'bg_yellow': '43m',  # Добавляем цвет фона к словарю
    'bg_blue': '44m',  # Добавляем цвет фона к словарю
    'bg_purpure': '45m',  # Добавляем цвет фона к словарю
    'bg_biruza': '46m',  # Добавляем цвет фона к словарю
    'bg_white': '47m',  # Добавляем цвет фона к словарю
}


def color_text(text, colour_name):
    """
    Окрашивает переданный текст в указанный цвет.

    :param text: Строка, которую нужно окрасить.
    :param colour_name: Название цвета (ключ из словаря 'colour').
    :return: Окрашенный текст с ANSI escape кодами.
    """
    coloured_txt = '\033[' + colour_name + text + '\033[0m'
    return coloured_txt


def styled(text, code="3m"):
    """
    Возвращает текст, стилизованный с помощью указанного ANSI escape кода.

    :param text: Строка, которую нужно стилизовать.
    :param code: ANSI escape код стиля (по умолчанию "3m").
    :return: Стилизованный текст с ANSI escape кодами.
    """
    clean_style_code = '\033[0m'
    styled_txt = f'\033[{code}{text}{clean_style_code}'
    return styled_txt


def error_message(message):
    """
    Создает сообщение об ошибке с определенными стилями и цветами.

    :param message: Сообщение об ошибке.
    :return: Сообщение об ошибке с ANSI escape кодами для стилизации.
    """
    status = "ERROR"
    error = color_text(f"{status:<8} ", colour['red'])
    _message = color_text(message, colour['yellow'])
    err_message = error + _message
    return err_message


def warning_message(message):
    """
    Создает предупреждающее сообщение с определенными стилями и цветами.

    :param message: Предупреждающее сообщение.
    :return: Предупреждающее сообщение с ANSI escape кодами для стилизации.
    """
    status = "WARNING"
    warn = color_text(f"{status:<8} ", colour['yellow'])
    _message = color_text(message, colour['biruza'])
    warn_message = warn + _message
    return warn_message


def info_message(message):
    """
    Создает информационное сообщение с определенными стилями и цветами.

    :param message: Информационное сообщение.
    :return: Информационное сообщение с ANSI escape кодами для стилизации.
    """
    status = "INFO"
    info = color_text(f"{status:<8} ", colour['purpure'])
    info_message = info + message
    return info_message


def universal_text_style(text_style='1', text_color='33m', bg_color='47m', text=None):
    bg_code = f'\033[{colour.get(bg_color)}'
    color_code = f'\033[{colour.get(text_color)}'
    style = f'\033[{text_style}m'
    styled_text = f'{style}{color_code}{bg_code}{text}\033[0m'
    return styled_text


if __name__ == "__main__":
    print(warning_message("упс, я снова ошибся"))
    print(error_message("неправильный путь"))
    print(info_message("спасибо за информацию"))
    print(universal_text_style("Мой тестовый шрифт"))
