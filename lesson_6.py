"""
# Задание 1
import time


class TrafficLight:

    def __init__(self, color):
        self.__color = color

    def running(self):
        print("Красный свет")
        time.sleep(7)
        print("Желтый свет")
        time.sleep(2)
        print("Зеленый свет")
        time.sleep(10)


super_man = TrafficLight("red")
print(super_man.running())



# Задание 2


class Road:
    def __init__(self, length, width):
        self.__length = length
        self.__width = width

    def calculation(self, weight, thickness):
        asphalt = int(self.__length * self.__width * weight * thickness / 1000)

        return asphalt


whole = Road(5000, 20)
print(whole.calculation(25, 5))



# Задание 3


class Worker:
    def __init__(self, name, surname, position, income):
        self.name = name
        self.surname = surname
        self.position = position
        self.__income = income


class Position(Worker):

    def get_full_name(self):
        print(self.name + " " + self.surname)

    def get_total_income(self):
        s = self._Worker__income
        d = sum(s.values())
        print(d)


a = Position("Саша", "Андреев", "Раб", {"wage": 10000, "bonus": 40000})
a.get_full_name()
a.get_total_income()




# Задание 4


class Car:

    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print("Машина поехала")

    def stop(self):
        print("Машина остановилась ")

    def turn(self, direction):
        print(f"Машина повернула {direction}")

    def show_speed(self):
        print(f"Ваша скорость: {self.speed}")


class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            print("Привышение скорости")
        else:
            print(f"Ваша скорость: {self.speed}")


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            print("Привышение скорости")
        else:
            print(f"Ваша скорость: {self.speed}")


class PoliceCar(Car):
    pass


a = WorkCar(10, "Чёрный", "ford", False)
print(a.is_police)
print(a.speed)
print(a.color)
print(a.name)

b = TownCar(100, "Чёрный", "BMW", False)
b.show_speed()
b.turn("В лево")
b.go()


"""

# Задание 5


class Stationery:

    def __init__(self, title):
        self.title = title

    def draw(self):
        print("Запуск отрисовки")


class Pen(Stationery):
    def draw(self):
        print("Рисуем портрет ручкой")


class Pencil(Stationery):
    def draw(self):
        print("Рисуем набросок карандашём")


class Handle(Stationery):
    def draw(self):
        print("Рисуем фон маркером")


a = Pen("Карандаш")
a.draw()
b = Pencil("Ручка")
b.draw()
c = Handle("Маркер")
c.draw()