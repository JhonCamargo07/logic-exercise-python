"""
Desarrollar un algoritmo que calcule el promedio de un arreglo de enteros (reales).
"""

import random


def create_list():
    nums = []
    for num in range(random.randint(7, 70)):
        nums.append(num)
    random.shuffle(nums)
    return nums


def add_list(nums):
    return sum(nums)


def avg_list(nums):
    print(nums)
    suma = add_list(nums)
    avg = suma / len(nums)
    return avg


if __name__ == '__main__':
    print(f'EL promedio de la lista es: {avg_list(create_list())}')
