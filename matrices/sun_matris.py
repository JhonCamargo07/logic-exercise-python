"""
Desarrollar un algoritmo que permita multiplicar dos matrices de nmeros reales (enteros)
"""


def get_array(num_matriz):
    print(f'Informacion de la {num_matriz}')
    nums_final = []

    str_num = input('Ingrese el array numero 1: ')
    nums = [int(num) for num in str_num]
    nums_final.append(nums)

    str_num = input('Ingrese el array numero 2: ')
    nums = [int(num) for num in str_num]
    nums_final.append(nums)

    return nums_final


def sum_matrices(matriz1, matriz2):
    matriz_final = []
    for mt1, mt2 in zip(matriz1, matriz2):
        matriz = []
        for nums_mt_1, nums_mt_2 in zip(mt1, mt2):
            matriz.append(nums_mt_1 + nums_mt_2)
        matriz_final.append(matriz)
    return matriz_final


if __name__ == '__main__':
    matriz1 = get_array('primera matriz')
    matriz2 = get_array('segunda matriz')
    print(matriz1)
    print(matriz2)
    print(sum_matrices(matriz1, matriz2))