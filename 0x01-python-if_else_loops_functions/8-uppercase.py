#!/usr/bin/python3
def uppercase(str):
    new_str = ""
    for i in range(len(str)):
        if (ord(str[i]) >= 97 and ord(str[i]) <= 122):
            new_str += chr(ord(str[i]) - 32)
            continue
            new_str += str[i]
        else:
            new_str += chr(ord(str[i]))
    print('{}'.format(new_str))