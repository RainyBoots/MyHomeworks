number = input('Введите номер телефона: ')
number_length = 11
report_string = ''

number_clean = number.replace('(', '').replace(')', '').replace('-', '').replace('+', '').replace(' ', '')


if len(number_clean) != 11:
    report_string += 'Некорректная длина номера\n'

if not (number_clean.startswith('8') or number_clean.startswith('7')):
    report_string += 'Номер должен начинаться только с +7 или 8\n'

if not number_clean.isdigit():
    report_string += 'Номер должен состоять только из чисел\n'

if report_string:
    print(f'Ваш номер не прошел проверку по причинам:\n{report_string:}')
else:
    print('Номер прошел проверку')


password = input('Введите пароль:')
report_string_2 = ''

if password.isalnum():
    report_string_2 += 'Пароль должен содержать хотя бы один спецзнак\n'

if password.count(' ') > 0:
    report_string_2 += 'Пароль не должен содержать пробелов\n'

if password.islower() or password.isupper():
    report_string_2 += 'Пароль должен содержать символы разных регистров\n'

if len(password) < 8:
    report_string_2 += 'Пароль должен быть более 7 символов длиной\n'

if report_string_2:
    print(f'Пароль  не надежный по причинам: {report_string_2}')
else:
    print('Пароль надежный')






