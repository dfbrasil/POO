# from passenger import Passenger
# from flight import Flight
# from operator import Operator

class Booking:

    def __init__(self, passenger, flight , operator )  -> None:

        self.__passenger = passenger
        self.__flight =  flight
        self.__operator = operator

    """getters"""
    def get_passenger(self) -> str:
        return self.__passenger

    def get_flight(self) -> str:
        return self.__flight

    def get_operator(self) -> str:
        return self.__operator

    """setters"""
    def set_passenger(self, new_passenger) -> None:
        self.__passenger = new_passenger

    def set_flight(self, new_flight) -> None:
        self.__flight = new_flight

    def set_operator(self, new_operator) -> None:
        self.__operator = new_operator

    def __str__(self) -> None:
        return (f'Passenger: \n{self.__passenger} \n\nFlight: \n{self.__flight}\n\nOperator: \n{self.__operator} \n')