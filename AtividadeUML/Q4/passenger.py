from person import Person

class Passenger(Person):

    """constructor"""
    def __init__(self, name : str, cpf : str, email_adress : str, phone_number : str, baggage_weight: float) -> None:
        super().__init__(name, cpf, email_adress, phone_number)
        self.__baggage_weight = baggage_weight

    """get"""
    def get_baggage_weight(self):
        return self.__baggage_weight

    """set"""
    def set_baggage_weight(self, baggage_weight):
        self.__baggage_weight = baggage_weight

    """str"""
    def __str__(self):
        return (f'\nName: {super().get_name()} \nCpf: {super().get_cpf()}\nEmail: {super().get_email_adress()} \nPhone: {super().get_phone_number()} \nBaggage Weight: {self.__baggage_weight}')

