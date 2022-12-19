#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    result = 0
    p = 0
    try:
        result = fct(*args)
        p = 1
    except BaseException as z:
        print("Exception: {}".format(z), file=sys.stderr)
    if p == 1:
        return result
    else:
        return None
