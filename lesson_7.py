"""""
# Задание 1
class Matrix:
    def __init__(self, arr):
        self.arr = arr

    def __str__(self):
        return f"Значение матрицы {self.arr}"

    def __add__(self, other):
        mass = []
        a_len = len(self.arr)
        a_w = len(self.arr[0])
        if a_len < len(other.arr):
            a_len = len(other.arr)
        if a_w < len(other.arr[0]):
            a_w = len(other.arr[0])

        for f in range(a_len):
            mass.append([0 for i in range(a_w)])


        for i in range(len(self.arr)):
            for j in range(len(self.arr[0])):
                mass[i][j] += self.arr[i][j]

        for i in range(len(other.arr)):
            for j in range(len(other.arr[0])):
                mass[i][j] += other.arr[i][j]

        return Matrix(mass)


a = Matrix([[7, 8, 9],
            [4, 5, 6],
            [1, 2, 3]])

b = Matrix([[7, 8],
            [4, 4],
            [1, 3],
            [1, 4]])
print(a + b)




# Задание 2

from abc import ABC, abstractmethod


class ClothingProduction(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod 
    def fabric(self):
        pass


class Coat(ClothingProduction):
    def __init__(self, name, size):
        super().__init__(name)
        self.size = size

    @property
    def summa(self):
        return self.__size

    @summa.setter
    def summa(self, size):
        if size < 2:
            print("Слишком маленькое значение")
        elif size > 10:
            print("Слишком большое значение")
        else:
            self.__size = size

    def fabric(self):
        i = self.size/6.5 + 0.5
        return f"{i:.2f}"


class Suit(ClothingProduction):
    def __init__(self, name, size):
        super().__init__(name)
        self.size = size

    @property
    def summa(self):
        return self.__size

    @summa.setter
    def summa(self, size):
        if size < 2:
            print("Слишком маленькое значение")
        elif size > 10:
            print("Слишком большое значение")
        else:
            self.__size = size

    def fabric(self):
        2 * self.size + 0.3

        return 2 * self.size + 0.3


a = Suit("Stile", 6)
print(a.fabric())
m = Coat("NewStile", 4)
print(m.fabric())


 """""

# Задание 3


class Cage:
    def __init__(self, cells):
        self.cells = cells

    def __add__(self, other):
        return Cage(self.cells + other.cells)

    def __str__(self):
        return f"Объект с параметрами ({self.cells})"

    def __sub__(self, other):
        if (self.cells - other.cells) < 0 and (other.cells - self.cells) < 0:
            return "Разница кол во клеток меньше нуля"
        else:
            return self.cells - other.cells

    def __mul__(self, other):
        return Cage(self.cells * other.cells)

    def __truediv__(self, other):
        return Cage(self.cells // other.cells)

    def make_order(self, row):
        a = ""
        for i in range(self.cells):
            a += "*"
            print(a)
        print(a)

        p = 0
        r = row
        while p < len(a):
            print(a[p:r] + "/n")
            p += row
            r += row


d = Cage(20)
print(d.make_order(4))
