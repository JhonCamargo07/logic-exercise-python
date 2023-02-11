"""
Encontrar los numeros primos del 1 al 1000
"""


def generate_nums(limit):
    nums = []
    for num in range(2, limit):
        nums.append(num)
    return nums


def get_nums_primos(nums: list):
    nums_primos = []
    for num in nums:
        if is_num_primo(num):
            nums_primos.append(num)
    return nums_primos


def is_num_primo(num):
    is_primo = True
    for n in range(2, num):
        if num % n == 0:
            is_primo = False
    return is_primo


if __name__ == '__main__':
    nums = generate_nums(1000)
    primos = get_nums_primos(nums)
    print(primos)
