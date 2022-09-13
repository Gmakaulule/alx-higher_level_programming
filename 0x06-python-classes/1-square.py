#!/usr/bin/python3
"""Definition of squre class"""


class Square:
    """This is the squre class
    Atributes:
    _size (int): length of squre
    """
    def __init__(self, size):
        """Initializes a square
        Args:
            size (int): size of a side of the square
        Returns: None
        """
        self.__size = size
