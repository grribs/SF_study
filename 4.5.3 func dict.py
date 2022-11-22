
def my_decorator(func):
    dict_cash = {}

    def wrapper(p):
        nonlocal dict_cash
        if p not in dict_cash:
           dict_cash[p] = func(p)
           print(f"Значение внесено в словарь: {dict_cash[p]}")
        else:
            print(f"Значение из словаря:{dict_cash[p]}")
            return dict_cash[p]
        print(f"Кэш {dict_cash}")
    return wrapper


def f(n):
    return n * 2


fn_sum = my_decorator(f)

fn_sum(4)

fn_sum(4)

fn_sum(5)