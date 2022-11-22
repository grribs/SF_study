
USERS = ['admin', 'guest', 'director', 'root', 'superstar']

yesno = input("""Введите Y, если хотите авторизоваться или N, 
если хотите продолжить работу как анонимный пользователь: \n""")

auth = yesno == "Y"
username = None

def is_auth(func):
    def wrapper():
        if auth and username is True:
            print("Прохождение авторизации:")
#            func()
        else:
            if auth is False:
                print("Пользователь неавторизован. Функция выполнена не будет")
    return wrapper


def has_access(func):
    def wrapper():
        if username in USERS:
            print("Доступ предоставлен")
            func()
        else:
            if auth:
                print("Пользователь не зарегистрирован.")
    return wrapper()




if auth:
    username = input("Введите ваш username:")

@is_auth
@has_access
def from_db():
    print("some data from database")

from_db()