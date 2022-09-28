#!/usr/bin/python3

'''return Json representation of an object'''
import json


def to_json_string(my_obj):
    '''serialise python object to JSON string'''
    return json.dumps(my_obj)
