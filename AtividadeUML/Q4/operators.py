from person import Person
from booking import Booking
from passenger import Passenger
from flight import Flight

class Operators(Person):

    def __init__(self, name : str, cpf : str, email_adress : str, phone_number : str, level : str) -> None:
        super().__init__(name, cpf, email_adress, phone_number)
        self.__level = level

    def new_booking(self, passenger : Passenger , flight : Flight):
        return Booking(passenger, flight, self)

    def __str__(self):
        return (f'Name: {self.get_name()} \nCpf: {self.get_cpf()} \nEmail: {self.get_email_adress()} \nPhone: {self.get_phone_number()}\nLevel: {self.__level}')