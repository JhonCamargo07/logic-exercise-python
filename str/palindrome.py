"""
Desarrollar un algoritmo que determina si una cadena de caracteres es frase pal´ındrome. Una
cadena se dice frase pal´ındrome si la cadena al eliminarle los espacios es pal´ındrome.
Ejemplos.
“anula las alas a la luna” es frase pal´ındrome.
“amor a roma” es frase pal´ındrome.
“dabale arroz a la zorra el abad” es frase pal´ındrome.
"""


def get_str_user():
    str_user = input('Ingrese la frase: ')
    return str_user


def replace_space_str(str_user: str):
    str_user = str_user.replace(' ', '')
    return str_user


def reverse_str(str_user: str):
    return str_user[len(str_user)::-1]


def is_str_palindromo(str_user, str_user_reverse):
    return str_user == str_user_reverse


if __name__ == '__main__':
    cadena = get_str_user()
    cadena_no_space = replace_space_str(cadena)
    print(f'Cadena sin espacios: {cadena_no_space}')
    new_cadena = reverse_str(cadena_no_space)
    print(f'Cadena sin espacios e invertida: {new_cadena}')

    print(f'La frase suministrado {"es" if is_str_palindromo(cadena_no_space, new_cadena) else "no es"} palindroma')
