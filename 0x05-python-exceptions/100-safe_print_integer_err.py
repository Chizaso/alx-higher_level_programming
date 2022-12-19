#!/usr/bin/python3
import sys


def safe_print_integer_err(value):
    p = False
    m = "Exception: Unknown format code 'd' for object of type 'str'\n"
    try:
        print("{:d}".format(value))
        p = True
    except (ValueError, TypeError) as m:
        print("Exception: {}".format(m), file=sys.stderr)
    return p
