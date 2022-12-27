
# a = 1234314465479
# d = a % 10
# print(d)


class Person:
    def print_info(self, n):
        for i in range(n):
            print(f"Name: {self.name}, Surname: {self.surname}, Place of birth: {self.place_of_birth}")

    def get_age(self, age):
        return print(age - self.year_of_birth)


p1 = Person()
p1.name = "Elon"
p1.surname = "Musk"
p1.place_of_birth = "ЮАР"
p1.year_of_birth = 1971


p1.get_age(2020)