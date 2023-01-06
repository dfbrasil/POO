class Person:

    def __init__(self, name : str, cpf : str, email_adress : str, phone_number : str):

        self.__name = name
        self.__cpf = cpf
        self.__email_adress = email_adress
        self.__phone_number = phone_number

    """getters"""
    def get_name(self) -> str:
        return self.__name

    def get_cpf(self) -> str:
        return self.__cpf

    def get_email_adress(self) -> str:
        return self.__email_adress

    def get_phone_number(self) -> str:
        return self.__phone_number

    """setters"""
    def set_name(self, new_name : str) -> None:
        self.__name = new_name

    def set_cpf(self, new_cpf : str) -> None:
        self.__cpf = new_cpf

    def set_email_adress(self, new_email_adress : str) -> None:
        self.__email_adress = new_email_adress

    def set_phone_number(self, new_phone_number : str) -> None:
        self.__phone_number = new_phone_number

    def __str__(self) -> str:
        return (f'Name: {self.__name} \nCpf: {self.__cpf}\nEmail: {self.__email_adress} \nPhone: {self.__phone_number}')