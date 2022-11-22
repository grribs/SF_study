

def my_decorator(fn):
    print("Этот код будет выведен один раз в момент декорирования функции")
    cntr = 0
    def wrapper(*args, **kwargs):
        print('Этот код будет выполняться перед каждым вызовом функции')
        fn(*args, **kwargs)
        nonlocal cntr
        cntr += 1
        print(f"Функция {fn} ,была вызвана {cntr} раз(а)")
    return wrapper


def say_word(word):
    print(word)


db_fn = my_decorator(say_word)


db_fn("Привет")

db_fn("Привет2")
