
def string(s):
    if len(s) == 1:
        return s
    return s[-1] + string(s[0:-1])


s = input()
print(string(s))
