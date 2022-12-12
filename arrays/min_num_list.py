"""
Desarrollar un algoritmo que calcule el m´ınimo de un arreglo de n´umeros enteros (reales).
"""

from avg_list import create_list


def num_min_list(nums):
    print(nums)
    return min(nums)


if __name__ == '__main__':
    print(f'El numero minimo del arreglo es: {num_min_list(create_list())}')
