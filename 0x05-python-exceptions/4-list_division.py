#!/usr/bin/python3


def list_division(my_list_1, my_list_2, list_length):
    p = []
    c = 0.0
    f = 0
    for i in range(0, list_length):
        c = 0
        try:
            c = my_list_1[i] / my_list_2[i]
            f = 1
        except ZeroDivisionError:
            print("division by 0")
            p += [0]
        except (TypeError):
            print("wrong type")
            p += [0]
        except IndexError:
            print("out of range")
            p += [0]
        finally:
            if f == 1:
                f = 0
                p += [c]
    return p
