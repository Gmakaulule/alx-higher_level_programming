#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    b_dictionary = a_dictionary.copy()

    for x, y in b_dictionary.items():
        b_dictionary[x] = y * 2
    return b_dictionary
