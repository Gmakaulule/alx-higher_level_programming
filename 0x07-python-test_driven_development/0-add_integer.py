if __name__ == "__main__":
    import doctest
    doctest.testfile("0-add_integer.txt")


def add_integer(a, b=98):
    """add two integers and return results"""
    if type(a) != int and type(a) != float:
        raise TypeError("a must be an integer")
    elif type(b) != int and type(b) != float:
        raise TypeError("b must be an integer")
    else:
        return int(a + b)
