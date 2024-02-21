seconds = int(input("Введите количество секунд: "))

hours = seconds // 3600
remains = seconds % 3600
minutes = remains // 60
remains = remains % 60

print(f"В указанном количестве секунд ({seconds}):\n "
      f"Часов: {hours}\n Минут: {minutes}\n Секунд: {remains} ")

temperature = int(input("Введите температуру в градусах цельсия: "))

Kelvin = temperature + 273.15

Fahrenheit = temperature * 1.8 + 32

Reaumur = temperature * 0.8

print(f"В указанном количестве градусов цельсия:{temperature}:\n"
      f"Градусов Кельвина: {round(Kelvin, 2)}\n"
      f"Градусов Фаренгейта: {round(Fahrenheit, 2)}\n"
      f"Градусов Реомюра: {round(Reaumur, 2)}")
