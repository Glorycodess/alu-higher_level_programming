#!/usr/bin/python3
  
def safe_print_list_integers(my_list=[], x=0):
    num = 0
    list_length = 0

    for _ in my_list:
        list_length += 1

    try:
        for item in range(x):
            print("{:d}".format(my_list[item]), end='')
            num += 1
    except IndexError:
        pass
    print()
    if x > list_length:
        raise IndexError("list index out of range")
    return num
