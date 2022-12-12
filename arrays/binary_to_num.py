"""
Suponga que un arreglo de enteros esta lleno de unos y ceros y que el arreglo representa un
n´umero binario al rev´es. Hacer un algoritmo que calcule los n´umeros en decimal que representa
dicho arreglo de unos y ceros.
Ejemplo.
    Entrada: (0, 1, 0, 1, 0, 1, 1) (representa el n´umero 1101010).
    Salida: 106
Ejemplo.
    Entrada: (1, 0, 0, 1, 0, 1, 1, 1, 1) (representa el n´umero 111101001).
    Salida: 389
"""


def get_list_num_binario():
    return list(input('Ingrese el numero binario al reves: '))


def revert_list(num_bin: list):
    num_bin.reverse()
    return num_bin


def convert_binary_to_num(num_bin):
    num_bin = "".join(num_bin)
    num_bin = int(num_bin, 2)
    return num_bin


if __name__ == '__main__':
    numero = convert_binary_to_num(revert_list(get_list_num_binario()))
    print(numero)
