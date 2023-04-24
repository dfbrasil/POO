from crew_role import Crew_Role
from person import Person


class Crew(Person):

    """constructor"""
    def __init__(self, name : str, cpf : str, email_adress : str, phone_number : str, role : Crew_Role) -> None:
        super().__init__(name, cpf, email_adress, phone_number)
        self.__role = Crew_Role(role)

    """get"""
    def get_role(self):
        return self.__role

    """set"""
    def set_role(self, new_role : Crew_Role):
        self.__role = new_role

    """str"""
    def __str__(self):
        return (f'\nName: {super().get_name()} \nRole: {self.__role.name}')