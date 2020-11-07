"""
# Задание 1
array = [1, 2.32, "Hello", [23, 16, 41], ("one", 3, 1997), {"a": 1, "b": 14, "c": 43}]

for el in array:
    print(type(el))

# Задание 2

newList = input("Введите через запятую желаемые элементы")
exchangeList = newList.split(",")
ray = 0
i = 0
j = 1
n = len(exchangeList)

if n % 2 != 0:
    n = n - 1

while i < n:
    ray = exchangeList[i]
    exchangeList[i] = exchangeList[j]

    exchangeList[j] = ray

    i += 2
    j += 2

print(exchangeList)


# Задание 3

month = int(input("Введите номер месяца, чтобы узнать время года: "))
season = ["Зима", "Весна", "Лето", "Осень"]

if month < 3 or month == 12:
    print(season[0])
elif month < 6:
    print(season[1])
elif month < 9:
    print(season[2])
elif month <= 11:
    print(season[3])


month = int(input("Введите номер месяца, чтобы узнать время года: "))
season = {"Зима": [1, 2, 12],
          "Весна": [3, 4, 5],
          "Лето": [6, 7, 8],
          "Осень": [9, 10, 11]}

for key in season:
    m = season[key]
    if month in m:
        print(key)

# Задание 4

lineValue = input("Введите строку из нескольких слов разделенных пробелами")
m = lineValue.split()

for i in enumerate(m):
    print(i[0]+1, i[1][:10])


# Задание 5
user = int(input("Введите число"))
mass = [7, 6, 5, 3, 3, 2]
i = 0
if user < mass[-1]:
    mass.append(user)
else:
    while i < len(mass):
        if user > mass[i]:
            mass.insert(i, user)
            break
        i += 1

print(mass)

"""
# Задание 6
cart = []

for i in range(3):

    inquiry = input("Введите через запятую : Название, цена, кол-во, единиц")

    m = inquiry.split(',')

    trial_list = {
        "Название": m[0],
        "цена":  m[1],
        "количество": m[2],
        "ед": m[3]
    }
    a = (i+1, trial_list)
    cart.append(a)
print(cart)

analytics = {
    "Название": [],
    "цена": [],
    "количество": [],
    "ед": []
}

for key in analytics:
    for i in cart:
        analytics[key].append(i[1][key])
print(analytics)
