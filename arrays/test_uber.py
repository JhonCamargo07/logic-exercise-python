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
        if 0 < num and num != count:
            return print(f'El numero faltante es: {count}')

        count += 1
    print(f'No falta ningún número')


if __name__ == '__main__':
    nums = [5, 4, 1, 1, 3, 2, 6, 7, -5, -2, 8, 9, 10, 19, 12, 13, 15, 14,-50, 16, 18, 17, 11, 20, 21, 30, -30, 0]
    get_minor_num(nums)
