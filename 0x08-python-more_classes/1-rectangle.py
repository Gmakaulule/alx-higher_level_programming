#!/usr/bin/python3
"""more classes and objects"""


class Rectangle:
    """This is an empty class"""
    def __init__(self, width=0, height=0):
        assert type(width) == int, f"width must be an integer "
        assert height >= 0, f"width must be an integer"
        self.__width = width
        self.__hight = height

    @property
    def width(self):
        """Retrieve width"""
        return self.__width

    @width.setter
    def width(self, value):

        """Set width"""
        if type(value) == int:
            self.__width = value
        else:
            raise ValueError('width must be an integer')

    @property
    def height(self):

        """Retrieve hight"""
        return self.__height

    @height.setter
    def height(self, value):
        """Set width"""
        if type(value) == int:
            self.__hight = value
        else:
            raise ValueError('height must be an integer')
