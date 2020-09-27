import random


MAX_N = 10 ** 5
MAX_K = 10 ** 5
MAX_VALUE = 10 ** 9


def generate_input(file_name):
    f = open(file_name, 'w')

    # N = random.randint(0, MAX_N)
    # K = random.randint(0, MAX_K)
    N = MAX_N
    K = MAX_K

    print(N, K, file=f)

    for _ in range(N):
        value = random.randint(0, MAX_VALUE)
        f.write(str(value) + ' ')

    f.write('')
    f.close()


generate_input('input03.txt')
