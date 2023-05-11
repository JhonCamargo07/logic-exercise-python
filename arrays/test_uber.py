'''
Dado un array de enteros no ordenado llamado nums, devuleve ele entero positivo mas pequeño que falte
'''


def get_minor_num(nums:list):
    nums.sort()
    nums = set(nums)
    count = 1
    print(f'Lista ordenada {list(nums)}')
    for num in nums:
        # print(f'El numero actual es {num} y el contador está en {count}')
        if 0 < num != count:
            return print(f'El numero faltante es: {count}')

        count += 1
    print(f'No falta ningún número')


nums = [5, 4, 1, 3, 2, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]


get_minor_num(nums)
