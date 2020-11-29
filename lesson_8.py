"""""
# Задание 1

class Data:
    def __init__(self, data):
        self.data = data

    @classmethod
    def date_generation(cls, data):
        cls.data = data
        day, month, year = map(int, cls.data.split("-"))
        print(day, month, year)

    @staticmethod
    def checking_values(day, month, year):
        if day > 31 or day < 0:
            print("Вы ввели не правильное значение дня")
        elif month > 12 or month < 0:
            print("Вы ввели не правильное значение месяца")
        elif year > 2020 or year < 2020:
            print("Вы ввели не правильное значение года")
        else:
            print(day, month, year)


w = Data("y")
w.date_generation("12-3-19")
Data.checking_values(12, 3, 2020)


# Задание 2

class Division(Exception):
    def __init__(self, tex):
        self.tex = tex


dividend = int(input("Введите делимое число: "))
divider = int(input("Введите делитель больше нуля: "))

try:
    d = dividend // divider

except ZeroDivisionError:
    print("На ноль делить нельзя")
else:
    print(f"Все хорошо. Результат - {d}")
finally:
    print("Программа завершена")


# Задание 3


class PresenceNumbers(Exception):
    def __init__(self, tex):
        self.tex = tex


arr = []


while True:
    use = input("Введите число: ")
    if use == "stop":
        print(arr)
        break
    try:
        if int(use) != int():
            arr.append(int(use))
        else:
            raise ValueError
    except ValueError:
        print("Вы ввели не число")

"""

# Задание 4


class EquipmentWarehouse:
    def __init__(self, name, quantity):
        self.name = name
        self.quantity = quantity
        self.test = {}

    def adoption(self, namez, quantityz):
        if type(self.quantity) == int:
            if namez in self.test:
                self.test[namez] = self.test[namez] + quantityz
            else:
                self.test[namez] = quantityz
        else:
            print("Введите количество техники цыфрой")
        return print(self.test)

    def transfer(self, nameTransfer, quantityTransfer ):
        if nameTransfer in self.test:
            if quantityTransfer < self.test[nameTransfer]:
                self.test[nameTransfer] = self.test[nameTransfer] - quantityTransfer
            else:
                print(f"Недостаточно {nameTransfer}")
        else:
            print("Нету на складе такой техники")
        return print(self.test)


class OfficeEquipment:
    def __init__(self, types, price):
        self.types = types
        self.price = price


class Printer(OfficeEquipment):
    def __init__(self, number, types, price):
        super().__init__(types, price)
        self.number = number


class Scanner(OfficeEquipment):
    def __init__(self, number, types, price):
        super().__init__(types, price)
        self.number = number


class Xerox(OfficeEquipment):
    def __init__(self, number, types, price):
        super().__init__(types, price)
        self.number = number


a = Printer(4, "Принтер", 8000)
b = Scanner(6, "Сканер", 4900)
d = Xerox(11, "Ксерокс", 6900)

house = EquipmentWarehouse("df", 1000)
house.adoption("Принтер", 2)
house.adoption("Принтер", 5)
house.transfer("Принтер", 10)




"""
# Задание 7


class Complex:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def com(self):
        comp = complex(self.a, self.b)
        a = comp
        return comp

    def __add__(self, other):
        return self.com() + other.com()

    def __mul__(self, other):
        return self.com() * other.com()


new = Complex(1, 2)
new2 = Complex(5, -4)
print(new * new2)

"""