"""
Desarrollar un algoritmo que reciba como entrada un carácter y de como salida el número de
ocurrencias de dicho car´acter en una cadena de caracteres.
"""


def get_answers_user():
    cadena = input('Ingrese la frase, oracion o parrado: ')
    character = input('¿Que caracter quiere buscar? ')
    return {'str': cadena, 'character': character}


def count_character_in_str(cadena, character):
    counter = 0
    for letter in cadena:
        if letter == character:
            counter += 1
    print(f'La letra \'{character}\' aparece {counter} veces')


if __name__ == '__main__':
    data = get_answers_user()
    count_character_in_str(data['str'], data['character'])
