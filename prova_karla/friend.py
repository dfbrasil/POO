from person import Person

class Friend(Person):
    def __init__(self, name, age, hobby):
        super().__init__(name, age)
        self.__hobby = hobby

    def chill(self):
        return f"{self.get_name()} is chilling"

    def play(self, friends):
        if len(friends) == 0:
            return f"jogar {self.__hobby}"
        elif len(friends) == 1: 
            return f"jogar {self.__hobby} com {friends[0]}"
        elif len(friends) == 2:
            return f"jogar {self.__hobby} com {friends[0]} e {friends[1]}"
        else:
            text = f"jogando {self.__hobby} com "

            counter = 0
            for friend in friends:
                if counter == len(friends) - 1:
                    text += f"e {friend}"
                else:
                    text += f"{friend}, "
                    counter += 1

            return text

    def __eq__(self, other):
        if self.get_name() == other.get_name() and self.get_age() == other.get_age() and self.get_hobby() == other.get_hobby():
            return True
        else:
            return False

    def __str__(self):
        return super().__str__() +  self.__hobby

    def get_hobby(self):
        return self.__hobby

    def set_hobby(self, hobby):
        self.__hobby = hobby

