"""
Desarrollar un algoritmo que calcule el producto directo de dos arreglos de enteros (reales) de
igual tama˜no. Sean v = (v1, v2, . . . , vn) y w = (w1, w2, . . . , wn) dos arreglos, el producto directo
de v y w (notado v ∗ w) es el vector: (v1 ∗ w1, v2 ∗ w2, . . . , vn ∗ wn).
"""
import random


def create_list(rang):
    nums = []
    for num in range(rang):
        nums.append(num)
    random.shuffle(nums)
    return nums


def product_list(list1, list2):
    final_list = []
    for lis1, lis2 in zip(list1, list2):
        final_list.append(lis1 * lis2)
    return final_list


if __name__ == '__main__':
    rang = random.randint(5, 70)

    list1 = create_list(rang)
    print(f'Lista 1\n {list1}')

    list2 = create_list(rang)
    print(f'Lista 2\n {list2}')

    print(f'Nueva lista:')
    print(product_list(list1, list2))
