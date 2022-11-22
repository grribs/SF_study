

def numb(s):
    if s < 10:
        return s
    else:
        return s % 10 + numb(s // 10)


s = int(input())
print(numb(s))
