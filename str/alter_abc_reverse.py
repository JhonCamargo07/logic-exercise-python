"""Desarrollar un algoritmo que decodifique una cadena de caracteres mediante una cadena de correspondencias de
caracteres dada. La cadena de correspondencias tiene como el primer car´acter el car´acter equivalente para el
car´acter ‘a’, el segundo car´acter para la ‘b’y as´ı sucesivamente hasta la ‘z’. No se tiene traducci´on para las
may´usculas ni para la ‘~n’.
Ejemplo.
    Entrada: “qs lxk rt Cgsgdwoq” y “qwertyuiopasdfghjklzxcvbnm”.
    Salida: “al sur de Colombia”.
Ejemplo.
    Entrada: “zg etw vb Ckgkhxsz” y “zxcvbnmasdfghjklqwertyuiop”.
    Salida: “al sur de Colombia”.
"""
import string

from alter_abc import *


def get_str_decrypted(str_user, abc_user):
    new_str = ""
    count = 0
    for letter in str_user:
        contador = 0
        for new_letter in abc_user:
            if letter == new_letter:
                new_str += abc[count]
            elif letter.isupper() and contador < 1:
                new_str += letter
            count += 1
            contador += 1
        contador = 0
        count = 0
    return new_str


if __name__ == '__main__':
    str_user = get_str_user()
    abc_user = get_abc_user()
    abc_user.append(' ')
    str_decrypted = get_str_decrypted(str_user, abc_user)
    print(str_decrypted)

