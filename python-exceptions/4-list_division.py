#!/usr/bin/python3


def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    for item in range(list_length):
        try:
            div = my_list_1[item] / my_list_2[item]
            new_list.append(div)
        except TypeError:
            print("wrong type")
            new_list.append(0)
        except ZeroDivisionError:
            print("division by zero")
            new_list.append(0)
        except IndexError:
            print("out of range")
            new_list.append(0)
    
    return new_list
