#!/usr/bin/python3
"""more classes and objects"""


class Rectangle:
    """This is an empty class"""
    def __init__(self, width=0, height=0):
        self.__width = width
        self.__hight = height

    @property
    def width(self):
        """Retrieve width"""
        return self.__width

    @width.setter
    def width(self, value):

        """Set width"""
        try:
            self.__width = value
        except self.__width < 0:
            raise ValueError

    @property
    def height(self):

        """Retrieve hight"""
        return self.__height

    @height.setter
    def height(self, value):
        """Set width"""
        try:
            self.__hight = value
        except self.__height < 0:
            raise ValueError
