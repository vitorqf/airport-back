from .person import Person

from marshmallow import Schema, fields, post_load


class Crew(Person, object):
    def __init__(self, name: str, occupation: str) -> None:
        super().__init__(name, __class__.__name__)
        self.__occupation = occupation

    def __str__(self) -> str:
        return f"Name: {self.name}, Occupation: {self.__occupation}"

    @property
    def occupation(self) -> str:
        return self.__occupation

    @occupation.setter
    def occupation(self, value) -> None:
        self.__occupation = value

class CrewSchema(Schema):
    name = fields.Str()
    occupation = fields.Str()

    @post_load
    def make_crew(self, data, **kwargs):
        return Crew(**data)