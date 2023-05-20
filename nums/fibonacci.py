"""
Dadiboo un natural, determinar si es un número de Fnacci o no.
"""


def get_num():
    try:
        return int(input('Ingrese el numero: '))
    except Exception as e:
        print(e)
        return get_num()


def is_fibonacci(num):
    num1 = num - 1
    num2 = num - 2

    if num1 + num2 == num:
        return True
    return False


if __name__ == '__main__':
    numero = get_num()
    print(f'el {numero} {"si es" if is_fibonacci(numero) else "no es"} fibonacci')
