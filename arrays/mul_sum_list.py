"""
Desarrollar un algoritmo que calcule el producto punto de dos arreglos de n´umeros enteros
(reales) de igual tama˜no. Sean v = (v1, v2, . . . , vn) y w = (w1, w2, . . . , wn) dos arreglos, el
producto de v y w (notado v ⋅ w) es el n´umero: v1 ∗ w1 + v2 ∗ w2 + ⋯ + vn ∗ wn.
"""

from product_list import *
from avg_list import add_list


if __name__ == '__main__':
    rang = random.randint(5, 70)

    list1 = create_list(rang)
    print(f'Lista 1\n {list1}')

    list2 = create_list(rang)
    print(f'Lista 2\n {list2}')

    final_list = product_list(list1, list2)
    print(f'\nNueva lista: \n{final_list}')

    print(f'\nResultado final: \n{add_list(final_list)}')
