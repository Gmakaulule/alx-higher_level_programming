#!/usr/bin/python3
"""more classes and objects"""


class Rectangle:
    """This is an empty class"""
    def __init__(self, width=0, hight=0):
        self.__width = width
        self.__hight = hight

    def width(self):
        """Retrieve width"""
        return self.__width

    def width(self, value):

        """Set width"""
        try:
            self.__width = value
        except self.__width < 0:
            raise ValueError

    def hight(self):

        """Retrieve hight"""
        return self.__hight

    def hight(self, value):
        """Set width"""
        try:
            self.__hight = value
        except self.__hight < 0:
            raise ValueError
