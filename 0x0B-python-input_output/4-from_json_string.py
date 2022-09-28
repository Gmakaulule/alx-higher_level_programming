#!/user/bin/pytho3

'''return object sructure'''
import json


def from_json_string(my_str):
    '''return json reprisentation of python data structre'''
    return json.dumps(my_str)
