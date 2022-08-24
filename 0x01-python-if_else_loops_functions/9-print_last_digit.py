#!/usr/bin/python3
def print_last_digit(number):
    number = abs(number)
    last_digit = number % 10
    if number < 0:
        number == abs(number)
        print(last_digit)
    else:
        print(last_digit)
        return last_digit
