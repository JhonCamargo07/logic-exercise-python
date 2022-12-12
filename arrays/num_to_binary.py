"""
Hacer un algoritmo que dado un n´umero entero no negativo, cree un arreglo de unos y ceros
que representa el n´umero en binario al rev´es.
Ejemplo.
    Número: 106
    Arreglo: (0, 1, 0, 1, 0, 1, 1) (representa el n´umero 1101010)
Ejemplo.
    N´umero: 389
    Arreglo: (1, 0, 0, 1, 0, 1, 1, 1, 1) (representa el n´umero 111101001)
"""


def get_list_num_binario():
    return input('Ingrese el numero: ')


def revert_list(num_bin: list):
    num_bin.reverse()
    return num_bin


def convert_num_to_binary(num):
    num_list = list(str(bin(int(num))))
    return num_list[2:]


if __name__ == '__main__':
    numero = revert_list(convert_num_to_binary(get_list_num_binario()))
    print(numero)
