class Person:
    def __init__(self, name, age):
        if age < 1 or age > 150:
            print("erro: a idade precisa estar no intervalo [1, 150]")
        else:
            self.__name = name
            self.__age = age

    def __str__(self):
        return f"{self.__name}({self.__age})"

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_age(self):
        return self.__age

    def set_age(self, age):
        self.__age = age

    pass
