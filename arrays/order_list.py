"""
Hacer un algoritmo que deje al final de un arreglo de n´umeros todos los ceros que aparezcan
en dicho arreglo.
Ejemplo.
vector original: (0, 11, 36, 10, 0, 17,−23, 81, 0, 0, 12, 11, 0)
vector salida: (11, 36, 10, 17,−23, 81, 12, 11, 0, 0, 0, 0, 0)
"""
from mul_sum_list import *


def remove_num_zero_list(nums):
    nums_zero = 0
    new_list = []
    for num in nums:
        if num != 0:
            new_list.append(num)
            continue
        nums_zero += 1
    return {'list': new_list, 'nums_zero': nums_zero}


def add_nums_zero_to_list(num):
    nums = []
    for data in range(num):
        nums.append(0)
    return nums


if __name__ == '__main__':
    rang = random.randint(5, 70)

    list1 = create_list(rang)
    list1.extend(add_nums_zero_to_list(random.randint(3, 10)))

    print(f'Lista\n{list1}')

    data_list = remove_num_zero_list(list1)
    list1 = data_list['list']
    list1.extend(add_nums_zero_to_list(data_list['nums_zero']))
    print(f'Lista final\n{list1}')



