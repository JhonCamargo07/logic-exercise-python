"""
Desarrollar un programa que sume los elementos de una columna dada de una matriz
"""
from sun_matris import get_array


def sum_column_matriz(matriz):
    matriz_result = []
    count = 0
    for mt1, mt2 in zip(matriz[0], matriz[1]):
        matriz_result.append(mt1 + mt2)
    return matriz_result


if __name__ == '__main__':
    matriz1 = get_array('primera matriz')
    for mt in matriz1:
        print(mt)
    print(sum_column_matriz(matriz1))