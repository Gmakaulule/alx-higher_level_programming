#!/usr/bin/python3

"""thi module read files"""


def read_file(filename=""):
    """file reader module"""

    with open(filename, encoding='utf-8') as f:
        for line in f:
            print(line, end="")
