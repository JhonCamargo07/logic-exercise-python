"""
Suma hasta cincuenta
Crea una variable que se llame total, después pide a tu usuario que ingrese un número y lo sume al valor de total.
Haz que esto se repita hasta que el valor de total sea mayor a 50 y muestra el resultado en pantalla.
"""


def get_num_user():
    try:
        return int(input('Ingrese el numero:\n'))
    except Exception as e:
        print(f'Error, vuelve a intentarlo: {e}')
        return get_num_user()


def sum_num():
    total = 0
    while total <= 50:
        total += get_num_user()
    print(f'El valor es {total}')


sum_num()
