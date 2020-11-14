
"""
# Задание 1

from sys import argv

script_name, hours_1, rate_2, award_3 = argv


def summa(hours, rate, award):
    hours = int(hours)
    rate = int(rate)
    award = int(award)
    salary = (hours * rate) + award
    return salary


print(summa(hours_1, rate_2, award_3))



# Задание 2

my_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
print(my_list)

new_list = [my_list[i+1] for i, el in enumerate(my_list[0:len(my_list)-2]) if el < my_list[i+1]]
print(new_list)




# Задание 3

mass_cra = [el for el in range(20, 240) if el % 20 == 0 or el % 21 == 0]
print(mass_cra)




# Задание 4

dav = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
dav_2 = [el_1 for i, el_1 in enumerate(dav) if el_1 not in dav[0:i] + dav[i+1:4]]
print(dav_2)




# Задание 5

from functools import reduce

mass_cra = [el for el in range(20, 1000) if el % 2 == 0]
print(mass_cra)


def numbers_sum(a, b):
    return a * b

print(reduce(numbers_sum,mass_cra))


# Задание 6.1

from itertools import count

user = int(input("Введите целое число от нуля до 25"))

for el in count(user):
    if el == 30:
        break
    else:
        print(el)




# Задание 6.2

from itertools import cycle

user_arr = input("Введите 5 чисел через пробел")
circular = user_arr.split()
counter = 0
print(circular)

for el in cycle(circular):
    print(el)
    counter += 1
    if counter == 25:
        break

"""

# Задание 7

q = 6


def fact(n):
    m = 1
    for i in range(1, n + 1):
        m = m * i
        yield m


for el in fact(q):
    print(el)
