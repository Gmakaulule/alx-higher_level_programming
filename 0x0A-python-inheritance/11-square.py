#!/usr/bin/python3

'''squre supoer class'''


BaseGeometry = __import__('7-base_geometry').BaseGeometry
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    '''squre properties and methods'''

    def __init__(self, size):
        self.integer_validator(size, size)
        super().__init__(size, size)
        self.__size = size

    def __str__(self):
        return '[Square] ' + str(self.__size) + '/' + str(self.__size)
