data_lst = ['1', '2', '3', '4d', 5]
new_list = []

for item in data_lst:
    try:
        new_item = int(item)
        new_list.append(new_item)
    except ValueError:
        print(f'Данные "{item}" невалидны')
print(new_list)

phone_numbers = input("Введите номера телефонов через точку с запятой без пробелов: ")
numbers = phone_numbers.split(';')

for number in numbers:
    number_clean = number.replace('(', '').replace(')', '').replace('-', '').replace('+', '').replace(' ', '')
    if len(number_clean) > 11:
        raise ValueError(f'Номер {number} больше 11 знаков')
    if not (number_clean.startswith('8') or number_clean.startswith('7')):
        raise ValueError(f'Номер {number} начинается не с +7 или 8')
    if not number_clean.isdigit():
        raise ValueError(f'Номер {number} состоит не только изи цифр')

