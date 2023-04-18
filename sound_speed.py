# sound_speed.py
medium = input("Введите тип среды: ")
if medium == "воздух":
    speed = 343
elif medium == "вода":
    speed = 1482
elif medium == "сталь":
    speed = 5000
else:
    print("Ошибка: неверный тип среды")
    speed = 0
print("Скорость звука в", medium, ":", speed, "м/с")
