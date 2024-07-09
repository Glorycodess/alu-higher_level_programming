#!/usr/bin/python3


def list_division(my_list_1, my_list_2, list_length):
    result_list = []

    for i in range(list_length):
        try:
            if i >= len(my_list_1) or i >= len(my_list_2):
                raise IndexError("out of range")

            dividend = my_list_1[i]
            divisor = my_list_2[i]

            if not (isinstance(dividend, (int, float)) and isinstance(divisor, (int, float))):
                raise TypeError("wrong type")

            try:
                result = dividend / divisor
            except ZeroDivisionError:
                result = 0

            result_list.append(result)

        except IndexError as e:
            print(f"out of range: {e}")
            result_list.append(0)

        except TypeError as e:
            print(f"wrong type: {e}")
            result_list.append(0)

        except Exception as e:
            print(f"Unexpected error: {e}")
            result_list.append(0)

    return result_list
