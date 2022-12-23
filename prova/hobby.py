from enum import Enum


class Hobby(Enum):
    music = 1
    sports = 2
    games = 3


    def print_my_hoby_is_games(hobby):
        if hobby == Hobby.games:
            print ('Meu hobby é ', hobby.name)
        else:
            print ('O hobby não é games e sim: ', hobby.name)
        return hobby.name


    