from C_181 import Cat
from C_181 import Client

c1 = Cat(name="Семён", sex="Мальчик", age="2")

cl1 = Client(name='Иван', surname='Петров', city='Москва', balance='50')
cl2 = Client(name='Сергей', surname='Сидоров', city='Москва', balance='40')

print(c1.get_name(), c1.get_sex(), c1.get_age())

print(cl1.get_client())


Clients = [cl1, cl2]

for i in Clients:
    print(i.get_client_corporate())

