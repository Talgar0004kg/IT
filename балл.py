Ваш_балл = int(input("Введите оценку за тест (0-100): "))

if Ваш_балл >= 90: 
    Домашка = input("Сдал ли студент все домашние задания? (да/нет): ")
    if Домашка == "да":
        print("Отлично! Оценка: A+")
    else:
        print("Хорошая работа, но сдайте все задания! Оценка: A")
elif 80 <= Ваш_балл < 90:
    Посещение = input("Посещал ли студент более 75% занятий? (да/нет): ")
    if Посещение.lower() == "да": 
        print("Хорошо! Оценка: B")
    else:
        print("Нужно посещать занятия! Оценка: C")
else:
    print("Старайтесь лучше!")
