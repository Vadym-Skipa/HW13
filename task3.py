# 3. Use Pool.apply() to get the row wise common items in list_a and list_b.
# list_a = [[1, 2, 3], [5, 6, 7, 8], [10, 11, 12], [20, 21]]
# list_b = [[2, 3, 4, 5], [6, 9, 10], [11, 12, 13, 14], [21, 24, 25]]

from multiprocessing import Pool, Process, current_process
from collections.abc import Iterable
from time import sleep


list_a = [[1, 2, 3], [5, 6, 7, 8], [10, 11, 12], [20, 21]]
list_b = [[2, 3, 4, 5], [6, 9, 10], [11, 12, 13, 14], [21, 24, 25]]


def check_iterable(obj):
    if isinstance(obj, (Iterable)):
        return True
    return False

def unpacking(obj):
    result = []
    if check_iterable(obj):
        for el in obj:
            result.extend(unpacking(el))
    else:
        result.append(obj)
    return result


def my_func(el, iterable: Iterable):
    print(current_process().name)
    if el in iterable:
        return el

with Pool() as pool:
    new_list_a = pool.apply(unpacking, args=(list_a,))
    new_list_b = pool.apply(unpacking, args=(list_b,))
    result = []
    for el in new_list_a:
        if pool.apply(func=my_func, args=(el, new_list_b)):
            result.append(el)
    print(result)





