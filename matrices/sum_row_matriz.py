"""
Desarrollar un programa que sume los elementos de una fila dada de una matriz
"""
from sun_matris import get_array


def sum_column_matriz(matriz):
    matriz_result = []
    count = 0
    for mt1, mt2 in matriz:
        matriz_result.append(mt1 + mt2)
        count += 1
    return matriz_result


if __name__ == '__main__':
    matriz1 = get_array('primera matriz')
    print(matriz1)
    print(sum_column_matriz(matriz1))