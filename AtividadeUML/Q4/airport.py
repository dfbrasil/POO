from city import City

class Airport:

    """constructor"""
    def __init__(self, name : str, city : City, takeoff_capacity : int) -> None:

        self.__name = name
        self.__city = city
        self.__takeoff_capacity = takeoff_capacity

    """getters"""
    def get_name(self) -> str:
        return self.__name

    def get_city(self) -> str:
        return self.__city

    def get_takeoff_capacity(self) -> str:
        return self.__takeoff_capacity

    """setters"""
    def set_name(self, new_name : str) -> None:
        self.__name = new_name

    def set_city(self, new_name_city : str, new_state : str, new_city : str) -> None:
        self.__city = City(new_name_city, new_state, new_city)

    def set_takeoff_capacity(self, new_takeoff_capacity : int) -> None:
        self.__takeoff_capacity = new_takeoff_capacity

    """str"""
    def __str__(self) -> str:
        return (f'Airport Name: {self.__name} \n{self.__city}')