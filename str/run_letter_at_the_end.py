"""
Desarrollar un algoritmo que realice el corrimiento circular a izquierda de una cadena de
caracteres. El corrimiento circular a izquierda es pasar el primer car´acter de una cadena como
´ultimo caracter de la misma.
Ejemplo.
    Entrada: “al sur de Colombia”.
    Salida: “l sur de Colombiaa”.
Ejemplo.
    Entrada: “Pepito va al colegio”.
    Salida: “epito va al colegioP”.
"""

from palindrome import get_str_user


def run_letter_at_the_end(str_user):
    first_letter = str_user[0]
    return str_user[1:] + first_letter


if __name__ == '__main__':
    str_user = get_str_user()
    print(f'La frase final es: {run_letter_at_the_end(str_user)}')

