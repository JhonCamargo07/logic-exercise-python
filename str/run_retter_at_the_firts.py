"""Desarrollar un algoritmo que realice el corrimiento circular a derecha de una cadena de caracteres. El
corrimiento circular a derecha de una cadena es poner el ´ultimo car´acter de la cadena como primer car´acter de la
misma.
Ejemplo.
    Entrada: “al sur de Colombia”.
    Salida: “aal sur de Colombi”.
Ejemplo.
    Entrada: “Pepito va al colegio”.
    Salida: “oPepito va al colegi”.

"""
from palindrome import get_str_user


def run_letter_at_the_first(phrase_user):
    first_letter = phrase_user[-1]
    return first_letter + phrase_user[:-1]


if __name__ == '__main__':
    str_user = get_str_user()
    print(f'La frase final es: {run_letter_at_the_first(str_user)}')
