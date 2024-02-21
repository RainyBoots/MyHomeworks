import json
from typing import Set, List, Optional


def read_city() -> Set[str]:
    """
    Функция загружает список городов из файла cities.json.
    """
    with open('cities.json', 'r', encoding='UTF-8') as file:
        return set(json.load(file))


def load_results() -> List:
    """
    Функция загружает список результатов из файла results.json.
    """
    try:
        with open("results.json", "r", encoding='UTF-8') as file:
            return json.load(file)
    except FileNotFoundError:
        return []


def save_results(results: List) -> None:
    """
    Функция записывает результат в results.json.
    """
    with open('results.json', 'w', encoding='UTF-8') as file:
        json.dump(results, file, ensure_ascii=False, indent=4)


def get_last_letter(city: str) -> str:
    """
    Функция для проверки на плохие буквы
    """
    non_letters = ('ь', 'ы', 'ш', 'й')
    if city.endswith(non_letters):
        return city[-2].capitalize()
    else:
        return city[-1].capitalize()


def validate_input_city(city: str, previous_char: Optional[str]) -> bool:
    """
    Функция для проверки пользователя на правильно введённый город.
    """
    if previous_char is not None and city[0] != previous_char:
        return True
    return False


def get_computer_city(city_name: Set[str], last_letter: str) -> Optional[str]:
    """
    Функция для выбора города компьютером.
    """
    for city in city_name:
        if city.startswith(last_letter):
            return city
    return None


def main() -> None:
    """
    Функция, которая описывает логику игры
    """
    results = load_results()
    for i, result in enumerate(results[-5:]):
        print(f"Игра {i + 1}: {result}")
    city_names = read_city()
    previous_char = None

    while True:
        input_city = input("Введите название города или 'Стоп' для завершения игры: ").capitalize()

        if input_city == "Стоп":
            print('Вы проиграли!!!')
            results.append('Победил компьютер!')
            break

        if validate_input_city(input_city, previous_char):
            print(f'Вы проиграли город должен начинаться с буквы {previous_char}')
            results.append('Победил компьютер!')
            break

        if input_city.capitalize() not in city_names:
            print('Победил компьютер')
            results.append('Победил компьютер!')
            break
        else:
            city_names.remove(input_city)

        last_letter = get_last_letter(input_city)

        computer_city = get_computer_city(city_names, last_letter)
        if computer_city is None:
            print('Вы победили!')
            results.append('Победил пользователь!')
            break
        else:
            city_names.remove(computer_city)

        previous_char = get_last_letter(computer_city)

        print(f'Компьютер выбрал город: {computer_city}')

    print('Конец игры')
    save_results(results)  # Функция для игры в города


if __name__ == "__main__":
    main()
