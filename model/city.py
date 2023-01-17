from marshmallow import Schema, fields, post_load

class City(object):
    def __init__(self, name: str, state: str, country: str) -> None:
        self.__name = name
        self.__state = state
        self.__country = country

    def __str__(self) -> str:
        return f"{self.__name}, {self.__state}, {self.__country}"

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, value: str) -> None:
        self.__name = value

    @property
    def state(self) -> str:
        return self.__state

    @state.setter
    def state(self, value: str) -> None:
        self.__state = value

    @property
    def country(self) -> str:
        return self.__country

    @country.setter
    def country(self, value: str) -> None:
        self.__country = value
        
class CitySchema(Schema):
    name = fields.Str()
    state = fields.Str()
    country = fields.Str()

    @post_load
    def make_city(self, data, **kwargs):
        return City(**data)