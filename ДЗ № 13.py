import csv
import re
from typing import Callable


def password_checker(func: Callable[[str], str]) -> Callable[[str], str]:
    """
    Декоратор, который проверяет пароль на соответствие определенным требованиям.
    Если пароль не соответствует одному или нескольким требованиям, возвращается соответствующее сообщение об ошибке.
    Если пароль соответствует всем требованиям, вызывается функция с переданным паролем и возвращается ее результат.
    """
    def wrapper(password: str) -> str:
        if len(password) < 8:
            return "Пароль должен содержать не менее 8 символов"
        if not any(char.isdigit() for char in password):
            return 'Пароль должен содержать хотя бы одну цифру'
        if not any(char.isupper() for char in password):
            return 'Пароль должен содержать хотя бы одну заглавную букву'
        if not any(char.islower() for char in password):
            return 'Пароль должен содержать хотя бы одну строчную букву'
        if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):  # Можно написать без регулярки,
            # но мне кажется так проще. Просто взял из интернета и все.
            return 'Ошибка: Пароль должен содержать хотя бы один спецсимвол'
        return func(password)
    return wrapper


@password_checker
def register_user(password: str) -> str:
    """
    Функция для регистрации пользователя
    """
    return 'Пользователь успешно зарегистрирован'


result = register_user('Password1!')
print(result)


def password_validator(min_length: int = 8, min_uppercase: int = 1, min_lowercase: int = 1, min_special_chars: int = 1)\
        -> Callable[[Callable[[str, str], None]], Callable[[str, str], None]]:
    """
    Декоратор, выполняющий валидацию пароля перед вызовом декорируемой функции.
    Возвращает декоратор, принимающий декорируемую функцию и возвращающий обертку.
    Если пароль проходит все проверки, вызывается декорируемая функция.
    """
    def decorator(func: Callable[[str, str], None]) -> Callable[[str, str], None]:
        def wrapper(username: str, password: str) -> None:
            if len(password) < min_length:
                raise ValueError(f"Пароль должен содержать не менее {min_length} символов.")
            if sum(char.isupper() for char in password) < min_uppercase:
                raise ValueError(f"Пароль должен содержать хотя бы {min_uppercase} символ(а) в верхнем регистре.")
            if sum(char.islower() for char in password) < min_lowercase:
                raise ValueError(f"Пароль должен содержать хотя бы {min_lowercase} символ(а) в нижнем регистре.")
            if sum(not char.isalnum() for char in password) < min_special_chars:
                raise ValueError(f"Пароль должен содержать хотя бы {min_special_chars} специальный символ.")
            return func(username, password)
        return wrapper
    return decorator


def username_validator(func: Callable[[str, str], None]) -> Callable[[str, str], None]:
    """
    Декоратор для проверки имени пользователя на отсутствие пробелов.
    Если имя не соответствует требованию то, выводит сообщение об ошибке.
    """
    def wrapper(username: str, password: str) -> None:
        if ' ' in username:
            raise ValueError('В имени пользователя не должно быть пробелов.')
        return func(username, password)
    return wrapper


@username_validator
@password_validator(min_length=8, min_uppercase=1, min_lowercase=1, min_special_chars=1)
def register_new_user(username: str, password: str) -> None:
    """
    Функция для записи пароля и имени пользователя в csv файл
    Спросил у чат бота не знаю как правильно написать, но вроде работает
    """
    with open('users.csv', 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([username, password])
    print('Успешная регистрация!')


try:
    register_new_user("JohnDoe", "Password123!")
    print("Регистрация прошла успешно!")
except ValueError as e:
    print(f"Ошибка: {e}")
