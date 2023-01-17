from marshmallow import Schema, fields, post_load

class Seat(object):
    def __init__(self, id: str, owner: str = 'Not owned', busy: bool = False) -> None:
        self.__id = id
        self.__busy = busy
        self.__owner = owner
    
    def __str__(self) -> str:
        return f"Is [{self.__id}] busy? {self.__busy}"

    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, value: str) -> None:
        self.__id = value

    @property
    def busy(self) -> bool:
        return self.__busy

    @busy.setter
    def busy(self, value: bool) -> None:
        self.__busy = value

    @property
    def owner(self) -> str:
        return self.__owner

    @owner.setter
    def owner(self, value: str) -> None:
        self.__owner = value

class SeatSchema(Schema):
    id = fields.Str()
    busy = fields.Bool()
    owner = fields.Str()

    @post_load
    def make_seat(self, data, **kwargs):
        return Seat(**data)