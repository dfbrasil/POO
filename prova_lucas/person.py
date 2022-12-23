class Person:

    """construtor"""
    def __init__(self, name, age):
        self.__name = name
        self.__age = age
        if not self.validation_age():
            print("Idade precisa estar entre 1 e 150")

    def validation_age(self):
        if self.__age > 0 and self.__age <= 150:
            return True
        else:
            return False
            
    """getters"""
    def get_name(self):
        return self.__name
    
    def get_age(self):
        return self.__age

    """setters"""
    def set_name(self, new_name):
        self.__name = new_name

    def set_age(self, new_age):
        self.__age = new_age

    """str"""
    def __str__(self):
        return self.__name + "(" + str(self.__age) + ")"
