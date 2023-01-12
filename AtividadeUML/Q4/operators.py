from person import Person
from booking import Booking
from passenger import Passenger
from flight import Flight

class Operators(Person):

    """constructor"""
    def __init__(self, name : str, cpf : str, email_adress : str, phone_number : str, level : str) -> None:
        super().__init__(name, cpf, email_adress, phone_number)
        self.__level = level

    """create new booking"""
    def new_booking(self, passenger : Passenger , flight : Flight) -> None:
        return Booking(passenger, flight, self)

    """str"""
    def __str__(self):
        return (f'Name: {self.get_name()} \nCpf: {self.get_cpf()} \nEmail: {self.get_email_adress()} \nPhone: {self.get_phone_number()}\nLevel: {self.__level}')