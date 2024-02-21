import json

from cities import cities_list
city_name = set()  # Переменная с сетом городов
non_letters = ('ь', 'ы', 'ш')  # Буквы с которых не может начинаться город
for city in cities_list:
    city_name.add(city["name"])  # Цикл для наполнения сета
previous_char = None  # Последняя или предпоследняя буква в городе который выбрал компьютер
try:
    with open("results.json", "r", encoding='UTF-8') as file:
        results = json.load(file)
        for i, result in enumerate(results[-5:]):
            print(f"Игра {i + 1}: {result}")  # Результат последних 5 игр
except FileNotFoundError:
    results = []  # Пробуем прочитать файл если файла нет то создаем пустой список с результатами
while True:
    input_city = input("Ведите название города или 'Стоп' для завершения игры: ")
    if input_city == "Стоп":
        print('Вы проиграли!!!')
        results.append('Победил компьютер!')
        break  # Если пользователь введет Стоп, то игра закончиться

    if previous_char is not None and input_city[0] != previous_char:
        print(f'Вы проиграли город должен начинаться с буквы {previous_char}')
        results.append('Победил компьютер!')
        break  # Если пользователь ввел город на неправильную букву, то игра завершается

    if input_city.capitalize() not in city_name:
        print('Победил компьютер')
        results.append('Победил компьютер!')
        break
    else:
        city_name.remove(input_city)  # Если пользователь ввел город которого нет в списке городов, то игра закончится
        # в противном случае этот город будет удален из сета

    if input_city.endswith(non_letters):
        last_letter = input_city[-2].capitalize()
    else:
        last_letter = input_city[-1].capitalize()  # Находим последнею или предпоследнею букву в слове

    computer_city = None  # Здесь будет город, который выберет компьютер

    for city in city_name:
        if city.startswith(last_letter):
            computer_city = city
            break  # Добавление города в переменную

    if computer_city is None:
        print('Вы победили!')  # Условие при котором побеждает пользователь
        results.append('Победил пользователь!')
        break
    else:
        city_name.remove(computer_city)

    if computer_city.endswith(non_letters):
        previous_char = computer_city[-2].capitalize()
    else:
        previous_char = computer_city[-1].capitalize()  # Последняя или предпоследняя буква в городе
        # который выбрал компьютер

    print(f'Компьютер выбрал город: {computer_city}')

print('Конец игры')

with open('results.json', 'w', encoding='UTF-8') as file:
    json.dump(results, file, ensure_ascii=False, indent=4)












