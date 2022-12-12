"""
Desarrollar un algoritmo que determine si una cadena de caracteres es pal´ındrome. Una cadena
se dice pal´ındrome si al invertirla es igual a ella misma.
Ejemplos.
    “ala” es pal´ındrome.
    “amor a roma” NO es palındrome.
    “al sur de Colombia” NO es pal´ındrome.
    “anula las alas a la luna” NO es pal´ındrome. (Al invertirla: “anul al a sala sal
    aluna”) no es igual a la original.
"""

from palindrome import *

if __name__ == '__main__':
    cadena = get_str_user()
    cadena_no_space = replace_space_str(cadena)
    print(f'Cadena sin espacios: {cadena_no_space}')
    new_cadena = reverse_str(cadena_no_space)
    print(f'Cadena sin espacios e invertida: {new_cadena}')

    print(f'La palabra suministrada {"es" if is_str_palindromo(cadena_no_space, new_cadena) else "no es"} palindrome')