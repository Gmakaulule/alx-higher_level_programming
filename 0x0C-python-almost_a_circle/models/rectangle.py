#!/usr/bin/python3

'''Importing Base class from file base.py'''
from models.base import Base


class Rectangle(Base):
    """Rectangle class with all properties and methods"""

    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        
        self.check_integer_parameter(width, 'width')
        self.check_integer_parameter(height, 'height')
        self.check_integer_parameter(x, 'x')
        self.check_integer_parameter(y, 'y')
    
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
        try:
            if type(width) == int:
                self.__width = width
        except:
            raise ValueError ('width must be an integer')
    @property
    def height_getter(self):
        '''get properties of height'''
        return self.__height

    def height_setter(self, height):
        '''set properties of height'''
        try:
            if type(height) == int:
                self.__height = height
        except:
            raise ValueError ("height must be an integer")
    def x_getter(self):
        '''get properties of x'''
        return self.__x

    def x_setter(self, x):
        """set properties of x"""
        try:
            if type(x) is int:
                self.__x = x
        except:
            raise ValueError ("x must be an integer")

    def y_getter(self):
        '''get properties of y'''
        return self.__y

    def y_setter(self, y):
        '''set properties of y'''

        raise ValueError ("y must be an integer")
    
    
    def check_integer_parameter(self, value, param):
        """
        ...
        """
        if type(value) is not int:
            raise TypeError(param + ' must be an integer')

        if value <= 0 and param in ('width', 'height'):
            raise ValueError(param + ' must be > 0')

        if value < 0 and param in ('x', 'y'):
            raise ValueError(param + ' must be >= 0')