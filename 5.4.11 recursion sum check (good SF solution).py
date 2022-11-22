
N = int(1234)
S = int(10)


def equal(N, S):
    print(N,S)
    if S < 0:
        return False
    if N < 10:
        return N == S
    else:
        return equal(N//10, S - N%10)


print(equal(N, S))

