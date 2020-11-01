# Задание номер 1

# name = input("Как ваше имя?")

# age = int(input("Сколько Вам Лет?"))

#   print(f"Привет {name} , вам {age} лет")


# Задание номер 2
"""
time = int(input("Введите время в секундах:"))

hours = time // 3600
seconds = time % 60
minutes = (time % 3600) // 60

if hours < 10:
    hours = "0" + str(hours)


if minutes < 10:
    minutes = "0" + str(minutes)


if seconds < 10:
    seconds = "0" + str(seconds)


print(hours, minutes, seconds)

# Задание 3

num = int(input("Введите число: "))

summa = num * 123

print(summa)



# Задание 4

integer = int(input("Введите целое число: "))
i = 1
a = 0
b = 0

while integer // i > 0:
    b = (integer % (i * 10) - integer % i) // i
    if b > a:
        a = b
    i = i * 10
print(f"Самое большое число: {a}")


# Задание 5

revenue = int(input("Введите значение выручки: "))
costsFirm = int(input("Введите значение издержки фирмы: "))
profitability = 0

if revenue > costsFirm:
    print("Выручка больше чем издержеки, фирма прибыльна")
    profitability = (revenue / costsFirm) % 100
    print("Рентабильность выручки : %.2f" % (profitability))
    workers = int(input("Количество сотрудников фирмы: "))
    profitWorkers = revenue / workers
    print(f"Прибыль фирмы на одного человека составляет : {profitWorkers}")
else:
    print("Издержки больше выручки, фирма убыточна")

"""
# Задание 6

a = int(input("В первый день результат составил: "))
b = int(input("Нужный результат : "))

day = 1

while a < b:
    a = (a * 1.1)
    day = day + 1

print("на %.0f день спортсмен достиг результата — не менее %.0f км." % (day, b))
