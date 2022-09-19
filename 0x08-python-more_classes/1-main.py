#!/usr/bin/python3
Rectangle = __import__('1-rectangle').Rectangle

my_rectangle = Rectangle(2, 5)
print(my_rectangle.__dict__)

my_rectangle.width = 8
my_rectangle.height = 1
print(my_rectangle.__dict__)
