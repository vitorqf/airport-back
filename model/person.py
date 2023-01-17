from marshmallow import Schema, fields


class Person:
    def __init__(self, name: str, func: str) -> None:
        self.__name = name
        self.__func = func

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, value: str) -> None:
        self.__name = value

    @property
    def func(self) -> str:
        return self.__func

    @func.setter
    def func(self, value: str) -> None:
        self.__func = value

class PersonSchema(Schema):
    name = fields.Str()
    func = fields.Str()