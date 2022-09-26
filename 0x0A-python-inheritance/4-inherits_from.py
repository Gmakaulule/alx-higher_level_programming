#!/usr/bin/python3

"""
check if is instance of a class
"""


def inherits_from(obj, a_class):
    """check if obj is instance of a_class"""

    if isinstance(obj, a_class) and \
       issubclass(a_class, obj.__class__) is False:
        return True

    return False
