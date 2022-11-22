

def numb(s):
    if len(s) == 1:
        return s
    p = 0
    p += int(s[-1])+int(numb(s[:-1]))
    return p

s = input()
print(numb(s))
