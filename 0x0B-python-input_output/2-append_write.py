#!/usr/bin/python3

'''apend mode in file input/output'''


def append_write(filename="", text=""):
    '''this module apend text at the end of file'''
    num_c = 0
    with open(filename, 'a', encoding="utf-8") as file:
        num_c = file.write(str(text))
        return num_c
