from type_flight import Type_Flight
from airport import Airport
from crew import Crew
from date import Date

class Flight:
    
    """constructor"""
    def __init__(self, code : str, free_seats : int, type : Type_Flight, origin_airport : Airport, destination_airport : Airport, year :int, month: int, day:int, hour:int, minute:int) -> None:

        self.__code = code
        self.__free_seats = free_seats
        self.__type_flight = Type_Flight(type)
        self.__crews = []
        self.__origin_airport = origin_airport
        self.__destination_airport = destination_airport
        self.__date_time = Date(year, month, day, hour, minute)

      
    """add crew on flight crew"""
    def add_crew(self, add_crew : Crew) -> None:
        self.__crews.append(add_crew)

    """remove crew on flight crew"""
    def remove_crew(self, remove_crew : Crew) -> None:
        for crew in self.__crews:
            if remove_crew == crew:
                self.__crews.remove(crew)
    
    """getters"""
    def get_code(self) -> str:
        return self.__code

    def get_free_seats(self) -> int:
        return self.__free_seats

    def get_type(self) -> str:
        return self.__type_flight

    def get_crews(self) -> str:
        crews = ''
        for crew in self.__crews:
            crews += str(crew)
        return crews

    def get_origin_airport(self) -> str:
        return self.__origin_airport

    def get_destination_airport(self) -> str:
        return self.__destination_airport

    def get_date_time(self):
        return self.__date_time

    """setters"""
    def set_code(self, new_code : str) -> None:
        self.__code = new_code

    def set_free_seats(self, new_free_seats : int)  -> None:
        self.__free_seats = new_free_seats

    def set_type(self, new_type : Type_Flight) -> None:
        self.__type_flight = Type_Flight(new_type) 

    def set_origin_airport(self, new_origin_airport : Airport) -> None:
        self.__origin_airport = new_origin_airport

    def set_destination_airport(self, new_destination_airport : Airport) -> None:
        self.__destination_airport = new_destination_airport

    def set_time(self, year, month, day, hour, minute):
        self.__date_time = (year, month, day, hour, minute)

    """str"""
    def __str__(self) -> str:
        return (f'Code: {self.__code} \nFree seats: {self.__free_seats}\nType: {self.__type_flight.name} \nDate: {self.__date_time.get_date()} \nHorário: {self.__date_time.get_time()} \nCrew\n[ {self.get_crews()}\n] \nOrigin: \n{self.__origin_airport} \nDestination: \n{self.__destination_airport} ')