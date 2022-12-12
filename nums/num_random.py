import random


def get_num_random():
    return random.randint(0, 99)


if __name__ == '__main__':
    for num in range(30):
        print(get_num_random())