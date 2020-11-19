"""
# Задание 1

while True:
    user = input("Введите данные:")
    with open("file.txt", "w+") as file:

        file.write(user)
    if user == "":
        break



# Задание 2

with open("files/file_2.txt", "r") as file:
    content = file.readlines()
    lines = len(content)
    print(lines)
    for el in content:
        arr_words = el.split()
        word = len(arr_words)
        print(word)


# Задание 3
summa = 0
peoples = []

with open("files/file_3.txt", "r", encoding="UTF-8") as file:
    lister = file.readlines()
    print(lister)
    for el in lister:
        list_arr = el.split()
        print(list_arr)
        summa = summa + float(list_arr[1])
        if float(list_arr[1]) > 20000:
            print(list_arr[0])
            peoples.append(list_arr[0])
print(summa / 10)
print(peoples)



# Задание 4

figures = ["Один", "Два", "Три", "Четыре"]
i = 0
with open("files/file_4.txt", "r", encoding="UTF-8") as file:
    while i < 4:
        lister = file.readlines()
        figure = lister.split()
        figure[0] = figures[i]
        lists_ru = ' '.join(figure)
        i += 1
        print(lists_ru)
        with open("files/file_4-1.txt", "a", encoding="UTF-8") as files:
            files.write(lists_ru + "\n")


# Задание 5

el_summa = 0

with open("files/file_5.txt", mode="w+") as file:
    file.write("12 43 31 8 44 6")
    file.seek(0)
    away = file.read()
    summa = away.split()
    for el in summa:
        elem = int(el)
        el_summa += elem

print(el_summa)



# Задание 6

figures = {}


with open("files/file_6.txt", "r", encoding="UTF-8") as file:
    content = file.readlines()
    for el in content:
        sum_items = 0
        elem = el.split()
        for i in range(1, 4):
            subject = elem[i][0:-(i+2)]
            if subject != "":
                sum_items += int(subject)
        figures[elem[0][0:-1] = sum_items
print(figures)

"""

# Задание 7
import json
list_firms = [{}, {}]

with open("files/file_7.txt", "r", encoding="UTF-8") as file:
    firms = file.readlines()
    print(firms)
    summa = 0
    i = 0
    for el in firms:
        firm = el.split()
        list_firms[0][firm[0]] = int(firm[2]) - int(firm[3])
        if int(firm[2]) - int(firm[3]) > 0:
            i += 1
            summa += int(firm[2]) - int(firm[3])
    list_firms[1]["average_profit"] = int(summa / i)
print(list_firms)


with open("files/file_7.1.json", "w") as write_f:
    json.dump(list_firms, write_f)
