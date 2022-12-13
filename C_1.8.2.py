from C_181 import Cat


class Dog(Cat):
    def get_pet(self):
        return f'{self.get_name()} {self.get_age()}'


c1 = Cat(name="Семён", sex="Мальчик", age="2")
d1 = Dog("Мухтар", "Мальчик", 0)


print(d1.get_pet())
