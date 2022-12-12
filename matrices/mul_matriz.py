"""
Desarrollar un algoritmo que permita multiplicar dos matrices de números reales (enteros)
"""

from sun_matris import get_array


def mul_matrices(matriz1, matriz2):
    matriz_final = []
    for mt1, mt2 in zip(matriz1, matriz2):
        matriz = []
        for nums_mt_1, nums_mt_2 in zip(mt1, mt2):
            matriz.append(nums_mt_1 * nums_mt_2)
        matriz_final.append(matriz)
    return matriz_final


if __name__ == '__main__':
    matriz1 = get_array('primera matriz')
    matriz2 = get_array('segunda matriz')
    print(matriz1)
    print(matriz2)
    print(mul_matrices(matriz1, matriz2))