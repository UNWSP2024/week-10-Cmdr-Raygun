# Author: Andrew Bittner
# Date: 11/2/2024
# Program: Triangle.py

class Triangle:
    def __init__(self, a, b, c):
        self.__a = a
        self.__b = b
        self.__c = c
    def get_perimeter(self):
        return self.__a + self.__b + self.__c
tri_1 = Triangle(9.237, 17.5, 5)
print(Triangle.get_perimeter(tri_1))