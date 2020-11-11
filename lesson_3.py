""""
# Задача 1

def division(a, b):
    if a == 0 or b == 0:
        return 0
    else:
        return int(a / b)


one = int(input("Введите первое число:"))
two = int(input("Введите второе число:"))

print(division(one, two))


# Задача 2

user = "Саша"
last_name = "Олов"
year = 19
city = "Москва"
email = "sasha@email.ru"
phone = 79783457654


def user_data(name1, last_name2, year3, city4, email5, phone6):
    print(name1, last_name2, year3, city4, email5, phone6)


user_data(name1=user, last_name2=last_name, year3=year, city4=city, email5=email, phone6=phone)



# Задача 3

number1 = input("Введите три  числа, через запятую")
number = number1.split(",")


def my_func(a):
    one = 0
    two = 0
    if int(a[0]) > int(a[1]):
        one = a[0]
        two = a[1]
    else:
        one = a[1]
        two = a[0]
    if int(two) < int(a[2]):
        two = a[2]
    return int(one) + int(two)


print(my_func(number))


# Задача 4.1

positive = int(input("Введите положительное число : "))
negative = int(input("Введите отрицательное число : "))


def my_func(x, y):
    i = -1
    a = 1
    while i >= y:
        a = a * x
        i = i - 1
    return 1 / a


print(my_func(positive, negative))



# Задача 4.2

positive = int(input("Введите положительное число : "))
negative = int(input("Введите отрицательное число : "))


def my_func(x, y):

    return x**y


print(my_func(positive, negative))



# Задача 6

word = input("Введите слово")


def int_func(x):

    x = x[0].upper() + x[1:]
    return x


print(int_func(word))

words = input("Введите слова")

words_arr = words.split(" ")
arr_title = ""

for el in words_arr:

    arr_title += int_func(el) + " "

print(arr_title)

"""

# Задача 5

sums = 0
bulls = True

while bulls is True:
    figures = input("Введите числа через пробел : ")

    figures_arr = figures.split()

    for el in figures_arr:
        if el == "q":
            bulls = False
            break

        sums = sums + int(el)

    print(sums)
