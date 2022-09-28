#!/bin/usr/python3

'''write a file and return number of charecers'''


def write_file(filename="", text=""):
    '''create a file and write on it'''

    with open(filename, 'w') as file:
        file.write(text)
        return len(text)
