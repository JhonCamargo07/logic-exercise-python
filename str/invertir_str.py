"""
Desarrollar un algoritmo que invierta una cadena de caracteres.
"""


def invertir_str(cadena_str):
    new_str = ''
    for letter in cadena_str:
        new_str = letter + new_str
    return new_str


if __name__ == '__main__':
    cadena = input('Ingrese la frase: ')
    print(invertir_str(cadena))
