word = input("Введите слово для проверки на палиндром: ")
new_string = word.lower().replace(" ", "")
reversed_string = new_string[::-1]
if new_string == reversed_string:
    print(f"Обнаружен палиндром: {word}")
else:
    print(f"{word} - не палиндром.")
