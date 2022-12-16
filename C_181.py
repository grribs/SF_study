class Cat:
    def __init__(self, name, sex, age):
        self.name = name
        self.sex = sex
        self.age = age

    def get_name(self):
        return self.name

    def get_sex(self):
        return self.sex

    def get_age(self):
        return self.age


class Client:
    def __init__(self, name, surname, city, balance):
        self.name = name
        self.surname = surname
        self.city = city
        self.balance = balance

    def get_client(self):
        return f'{self.name} {self.surname}. {self.city}. Баланс: {self.balance} руб.'

    def get_client_corporate(self):
        return self.name, self.surname, self.city




    # more correct SF
    # def __str__(self):
    #     return f'''"{self.first_name} {self.second_name}". {self.city}. Баланс: {self.balance} руб.'''
