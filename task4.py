# 4. Divide the work between 2 methods: print_cube that returns the cube of number
# and print_square that returns the square of number. These two methods should be executed
# by using 2 different processes.

from concurrent.futures import ProcessPoolExecutor
from multiprocessing import current_process

def print_cube(number):
    cube = pow(number, 3)
    print(cube, current_process().name)
    return cube

def print_square(number):
    square = pow(number, 2)
    print(square, current_process().name)
    return square

with ProcessPoolExecutor() as executor:
    cube = executor.submit(print_cube, 7)
    square = executor.submit(print_square, 7)
