# Определение словаря 'colour', который сопоставляет названия цветов.
colour = {
    'red': '31m',
    'black': '30m',
    'green': '32m',
    'yellow': '33m',
    'blue': '34m',
    'purpure': '35m',
    'biruza': '36m',
    'white': '37m'
}


def color_text(text, colour_name):
    """Определение функции 'color_text', которая принимает аргументы 'text' и 'colour_name'
    и возвращает 'text' с указанным цветом, используя коды ANSI escape."""
    coloured_txt = '\033[' + colour_name + text + '\033[0m'
    return coloured_txt


def styled(text, code="3m"):
    """Определение функции 'styled', которая принимает аргументы 'text' и 'code' (по умолчанию "3m")
    и возвращает 'text' с применением указанного кода."""
    clean_style_code = '\033[0m'
    styled_txt = f'\033[{code}{text}{clean_style_code}'
    return styled_txt


def error_message(message):
    """Определение функции 'error_message', которая создает сообщение об ошибке с префиксом "ERROR"
    и окрашивает его в красный цвет, а также окрашивает текст ошибки в желтый цвет."""
    status = "ERROR"
    error = color_text(f"{status:<8} ", colour['red'])
    _message = color_text(message, colour['yellow'])
    err_message = error + _message
    return err_message


def warning_message(message):
    """Определение функции 'warning_message', которая создает предупреждающее сообщение с префиксом "WARNING"
    и окрашивает его в желтый цвет, а также окрашивает текст предупреждения в бирюзовый цвет."""
    status = "WARNING"
    warn = color_text(f"{status:<8} ", colour['yellow'])
    _message = color_text(message, colour['biruza'])
    warn_message = warn + _message
    return warn_message


def info_message(message):
    """Определение функции 'info_message', которая создает информационное сообщение с префиксом "INFO"
    и окрашивает его в фиолетовый цвет."""
    status = "INFO"
    info = color_text(f"{status:<8} ", colour['purpure'])
    info_message = info + message
    return info_message


"""
Example:
s = "\033[3m"
c = "\033[33m"
f  = "\033[41m";
clean = "\033[0m"
pattern = f"{s}{c}{f}{txt}{clean}"
"""

if __name__ == "__main__":
    '''Пример использования функций для вывода сообщений разных типов с цветами.'''
    print(warning_message("ups i did sit again"))
    print(error_message("wrong way"))
    print(info_message("thanks for info"))
