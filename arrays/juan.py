"""
Encontrar el numero faltante de un array de enteros
[2, 3, 4, 5] - 3
"""


def get_num_faltente(array, rango):
    array.sort()
    if len(array) > rango:
        print("Error de negocio")
        return

    list1 = []
    for num in range(len(array)):
        list1.append(num)

    # print(list1, array)
    for num in range(rango):
        if num >= len(array):
            break
        if array[num] != list1[num]:
            print(f'Numero faltante: {list1[num]}')
            return
    print("No falta ningun numero")


array = [0, 1, 2, 3, 5]
get_num_faltente(array, 7)
