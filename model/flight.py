from uuid import uuid4

from .airport import Airport
from .crew import Crew
from .seat import Seat

from marshmallow import Schema, fields, post_load

import datetime

class Flight:
    def __init__(self, type: str, departure: Airport, destination: Airport, departure_time: datetime.time, departure_date: datetime.date, seats: dict[str, Seat], crew: list[Crew]) -> None:
        self.__id = uuid4()
        self.__type = type
        self.__departure = departure
        self.__destination = destination
        self.__departure_time = departure_time
        self.__departure_date = departure_date
        self.__seats = seats
        self.__crew = crew

    def freeSeats(self) -> dict[str, Seat]:
        return [seat for seat in self.__seats if seat.busy == False]

    def showCrew(self):
        return [(crew_member) for crew_member in self.__crew]

    def __str__(self):
        return f"ID: {self.__id}\
               \nTYPE: {self.__type}\
               \nTRAVEL: {self.__destination.name} -> {self.__departure.name}\
               \nDEPARTURE DATE: {self.__departure_date.strftime('%d/%m/%Y')}\
               \nDEPARTURE AT: {self.__departure_time}"
    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, value) -> None:
        self.__id = value

    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, value: str) -> None:
        self.__type = value


    @property
    def departure(self) -> Airport:
        return self.__departure

    @departure.setter
    def departure(self, value: Airport) -> None:
        self.__departure = value

    @property
    def destination(self) -> Airport:
        return self.__destination

    @destination.setter
    def destination(self, value: Airport) -> None:
        self.__destination = value

    @property
    def departure_time(self) -> datetime.time:
        return self.__departure_time

    @departure_time.setter
    def departure_time(self, value: datetime.time) -> None:
        self.__departure_time = value

    @property
    def departure_date(self) -> datetime.date:
        return self.__departure_date

    @departure_date.setter
    def departure_date(self, value: datetime.date) -> None:
        self.__departure_date = value

    @property
    def seats(self) -> dict[str, Seat]:
        return self.__seats

    @seats.setter
    def seats(self, value: dict[str, Seat]) -> None:
        self.__seats = value

class FlightSchema(Schema):
    id = fields.Str()
    type = fields.Str()
    departure = fields.Nested('AirportSchema')
    destination = fields.Nested('AirportSchema')
    departure_time = fields.Time()
    departure_date = fields.Date()
    seats = fields.Nested('SeatSchema', many=True)
    crew = fields.Nested('CrewSchema', many=True)

    @post_load
    def make_flight(self, data, **kwargs):
        return Flight(**data)