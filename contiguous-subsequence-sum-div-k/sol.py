def read_input(file_name):
    f = open(file_name, 'r')

    _, K = map(int, f.readline().split())

    a = list(map(int, f.readline().split()))

    f.close()

    return a, K


def write_output(file_name, R):
    f = open(file_name, 'w')
    print(R, file=f)
    f.close()


def init(a, K):
    amod = [0] * len(a)
    amod[0] = a[0] % K

    for i in range(1, len(a)):
        amod[i] = (amod[i - 1] + a[i]) % K

    p = [-1] * K

    return amod, p


def solve(a, K):
    res = 0

    amod, p = init(a, K)
    N = len(amod)

    for i in range(N):
        value = amod[i]

        if value > 0 and p[value] < 0:
            p[value] = i

    for i in range(N):
        value = amod[i]
        res = max(res, i - p[value])

    return res


#######################################


for i in range(1, 4):
    inp_file_name = f'input{i:02d}.txt'
    out_file_name = f'output{i:02d}.txt'

    a, K = read_input(inp_file_name)

    res = solve(a, K)

    write_output(out_file_name, res)
