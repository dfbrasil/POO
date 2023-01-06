from person import Person
from crew_role import Crew_Role

class Crew(Person):

    def __init__(self, name : str, cpf : str, email_adress : str, phone_number : str, role : Crew_Role) -> None:
        super().__init__(name, cpf, email_adress, phone_number)
        self.__role = Crew_Role(role)

    """get"""
    def get_role(self):
        return self.__role

    """set"""
    def set_role(self, new_role : Crew_Role):
        self.__role = new_role

    def __str__(self):
        return (f'\nName: {super().get_name()} \nCpf: {super().get_cpf()}\nEmail: {super().get_email_adress()} \nPhone: {super().get_phone_number()} \nRole: {self.__role.name}')