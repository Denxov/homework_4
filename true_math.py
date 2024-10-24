from math import inf
def divide(first,second):
    try:
        x = first / second
    except ZeroDivisionError:
        x = inf
    return x
