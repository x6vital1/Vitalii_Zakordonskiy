def is_valid_password(password):
    if password is None:
        return False
    if len(password) < 8:
        return False
    has_digit = False
    has_letter = False
    has_special_char = False
    for char in password:
        if char.isdigit():
            has_digit = True
        elif char.isalpha():
            has_letter = True
        elif char in "!@#$%^&*()_+{}[]:;<>,.?~\\":
            has_special_char = True
        if char in ' \t':
            return False
    return has_digit and has_letter and has_special_char


def password_requirements(func):
    def wrapper():
        print(
            "Пароль должен содержать хотя бы 1 цифру, 1 букву, 1 спец символ и быть не менее 8 символов в длину.")
        result = func()
        while not is_valid_password(result):
            if result is None:
                print(
                    "Пустую строку вводить нельзя. Пробельные символы и символы табуляции не допускаются.")
            else:
                missing_requirements = []
                if len(result) < 8:
                    missing_requirements.append("пароль короче 8 символов")
                if not any(
                        char.isdigit() for char in result):
                    missing_requirements.append("отсутствует цифра")
                if not any(
                        char.isalpha() for char in result):
                    missing_requirements.append("отсутствует буква")
                if not any(
                        char in "!@#$%^&*()_+{}[]:;<>,.?~\\" for char in result):
                    missing_requirements.append("отсутствует специальный символ")
                if any(
                        char in ' \t' for char in result):
                    missing_requirements.append("присутствует пробел или табуляция")
                print(
                    f"Пароль не соответствует требованиям: {', '.join(missing_requirements)}", "!")
            result = func()
        print("Пароль соответствует требованиям.")
        return result

    return wrapper


@password_requirements
def get_password():
    input_password = input("Введите пароль: ")
    if not input_password.strip():
        return None
    return input_password


password_result = get_password()
print("Введенный пароль:", password_result)
