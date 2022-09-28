#!/usr/bin/python3


"""
A module that write object to text file
"""
import json


def save_to_json_file(my_obj, filename):
    """
    Writing into filename that value ot text
    """
    num_of_char = 0
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(json.dumps(my_obj))
