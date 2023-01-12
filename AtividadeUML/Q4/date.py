import datetime

class Date:

    """constructor"""
    def __init__(self, year :int, month: int, day:int, hour:int, minute:int) -> None:
        self.__date = datetime.date(year,month,day)
        self.__time = datetime.time(hour,minute)

    """get"""
    def get_date(self):
        return self.__date
    
    def get_time(self):
        return self.__time

    """set"""
    def set_date(self, year, month, day):
        self.__date = (year,month,day)

    def set_time(self, hour, minute):
        self.__time = (hour,minute)

    """str"""
    def __str__(self) -> str:
        return (f'Day: {self.__date.year}/{self.__date.month}/{self.__date.day}\n Hour: {self.__time.hour}:{self.__time.minute}')
