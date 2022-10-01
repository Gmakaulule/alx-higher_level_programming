#!/usr/bin/python3

'''Importing Base class from file base.py'''
from models.base import Base


class Rectangle(Base):
    """Rectangle class with all properties and methods"""

    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)

        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        self.__id = id

    @property
    def width_getter(self):
        '''get the properties of width'''
        return self.__width

    def width_setter(self, width):
        '''set properties of width'''
        self.__width = width

    def height_getter(self):
        '''get properties of height'''
        return self.__height

    def height_setter(self, height):
        '''set properties of height'''
        self.__height = height

    def x_getter(self):
        '''get properties of x'''
        return self.__x

    def x_setter(self, x):
        """set properties of x"""
        self.__x = x

    def y_getter(self):
        '''get properties of y'''
        return self.__y

    def y_setter(self, y):
        '''set properties of y'''
        self.__y = y
