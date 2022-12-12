"""
Desarrollar un algoritmo que determine la mediana de un arreglo de enteros (reales). La
mediana es el n´umero que queda en la mitad del arreglo despu´es de ser ordenado.
"""

from mul_sum_list import *


def median_list(nums):
    size_list = int(len(nums))
    print(f'\nTamaño total lista: {size_list} \nMitad de la lista: {size_list / 2}\n')
    if len(nums) % 2 == 0:
        position_list = int(len(nums) / 2)
        return nums[position_list-1:position_list+1]
    else:
        position_list = int(len(nums) / 2)
        return nums[position_list]


if __name__ == '__main__':
    rang = random.randint(5, 70)

    list1 = create_list(rang)
    print(f'Lista\n{list1}')
    print(f'La mediana es: {median_list(list1)}')
