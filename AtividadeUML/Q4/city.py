class City:
    
    """constructor"""
    def __init__(self, name : str, state : str, country : str) -> None:

        self.__name = name
        self.__state = state
        self.__country = country

    """getters"""
    def get_name(self) -> str:
        return self.__name

    def get_state(self) -> str:
        return self.__state

    def get_country(self) -> str:
        return self.__country

    """setters"""
    def set_name(self, new_name : str) -> None:
        self.__name = new_name

    def set_state(self, new_state : str) -> None:
        self.__state = new_state

    def set_country(self, new_country : str) -> None:
        self.__country = new_country

    """str"""
    def __str__(self):
        return (f'City Name: {self.__name} \nState: {self.__state}\nCountry: {self.__country}')