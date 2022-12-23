from person import Person
from hobby import Hobby

class Friend(Person):

    def __init__(self, name, age, hobby):
        super().__init__(name, age)
        self.__hobby = hobby

    """getters"""
    def get_hobby(self):
        return self.__hobby

    """setters"""
    def set_hobby(self, new_hobby):
        self.__hobby = new_hobby

    """str"""
    def __str__(self):
        return super().get_name() + " " + str(super().get_age()) + " " + str(self.__hobby)

    """método chilli"""
    def chill(self):
        return super().get_name() + " is chilling" 

    "método play"
    def play(self, list_friends):
        if len(list_friends) == 0:
            return "jogar " +  str(self.__hobby)
        elif len(list_friends) == 1:
            string = "jogar " + str(self.__hobby) 
            for i in list_friends:
                string = string + " com  " + i.get_name()

            return string
        elif len(list_friends) == 2:
            string = "jogar " + str(self.__hobby) 
            for i in list_friends:
                string = string + " com  " + i.get_name()

            return string
        elif len(list_friends) >= 3:
            string = "jogar " + str(self.__hobby) 
            for i in list_friends:
                string = string + " com  " + i.get_name()

            return string
    
    """eq"""
    def __eq__(self, other):
        if self.get_name() == other.get_name() and self.get_age() == other.get_age() and self.__hobby == other.__hobby:
            return True
        else:
            return False
