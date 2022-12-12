"""Desarrollar un algoritmo que codifique una cadena de caracteres mediante una cadena de correspondencias de
caracteres dada. La cadena de correspondencias tiene como el primer car´acter el car´acter equivalente para el
car´acter ‘a’, el segundo car´acter para la ‘b’y as´ı sucesivamente hasta la ‘z’. No se tiene traducci´on para las
may´usculas ni para la ‘Ñ’.
Ejemplo.
    Entrada: “al sur de Colombia” y “qwertyuiopasdfghjklzxcvbnm”.
    Salida: “qs lxk rt Cgsgdwoq”.
Ejemplo.
    Entrada: “al sur de Colombia” y “zxcvbnmasdfghjklqwertyuiop”.
    Salida: “zg etw vb Ckgkhxsz”.
"""
import string

abc = list(string.ascii_lowercase)
abc.append(' ')


def get_str_encrypted(str_user, abc_user):
    new_str = ""
    count = 0
    for letter in str_user:
        contador = 0
        for old_letter in abc:
            if letter == old_letter:
                new_str += abc_user[count]
            elif letter.isupper() and contador < 1:
                new_str += letter
            count += 1
            contador += 1
        contador = 0
        count = 0
    return new_str


def get_str_user():
    string_user = input('Ingrese la frase: ')
    return list(string_user)


def get_abc_user():
    abc_user = input('Ingrese el abecedario: ')
    return list(abc_user)


if __name__ == '__main__':
    str_user = get_str_user()
    abc_user = get_abc_user()
    abc_user.append(' ')
    str_encrypted = get_str_encrypted(str_user, abc_user)
    print(str_encrypted)

