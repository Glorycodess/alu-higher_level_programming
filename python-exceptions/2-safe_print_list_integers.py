#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    num = 0
    list_length = 0
    
    for _ in my_list:
        list_length += 1
    
    for item in range(min(x, list_length)):
        try:
            print("{:d}".format(my_list[item]), end='')
            num += 1
        except (ValueError, TypeError):
            pass
    print()
    return num
