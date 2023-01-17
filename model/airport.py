from marshmallow import post_load, fields, Schema

from .city import City, CitySchema

class Airport(object):
    def __init__(self, city: City, max_departures: int, name: str) -> None:
        self.__city = city
        self.__max_departures = max_departures
        self.__name = name

    def __str__(self):
        return f"{self.__name}\nMax departures per hour: {self.__max_departures}\n{self.__city}\n"

    @property
    def city(self) -> City:
        return self.__city
    
    @city.setter
    def city(self, value: City) -> None:
        self.__city = value

    @property
    def max_departures(self) -> int:
        return self.__max_departures

    @max_departures.setter
    def max_departures(self, value: int) -> None:
        self.__max_departures = value

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, value: str) -> None:
        self.__name = value

class AirportSchema(Schema):
    city = fields.Nested(CitySchema)
    max_departures = fields.Int()
    name = fields.Str()

    @post_load
    def make_airport(self, data, **kwargs):
        return Airport(**data)
