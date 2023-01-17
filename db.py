import datetime
from uuid import uuid4

city_list = [
    {
        "name": "Guarulhos",
        "state": "Sao Paulo",
        "country": "Brazil",
    },
    {
        "name": "Los Angeles",
        "state": "California",
        "country": "United States",
    },
    {
        "name": "Sao Paulo",
        "state": "Sao Paulo",
        "country": "Brazil",
    },
    {
        "name": "Recife",
        "state": "Pernambuco",
        "country": "Brazil",
    }
]

airport_list = [
    {
        "city": city_list[0],
        "max_departures": 10,
        "name": "Guarulhos International Airport"
    },
    {
        "city": city_list[1],
        "max_departures": 10,
        "name": "Los Angeles International Airport"
    },
    {
        "city": city_list[3],
        "max_departures": 10,
        "name": "Recife International Airport"
    }
]

flight_list = [
    {
        "id": str(uuid4()),
        "type": "International",
        "departure": airport_list[0],
        "destination": airport_list[1],
        "departure_time": datetime.time(8),
        "departure_date": datetime.date(2022, 10, 28),
        "seats": [
            {
                "id": "A11",
            },
            {
                "id": "A12",
            },
            {
                "id": "A13",
            },
            {
                "id": "B11",
            },
            {
                "id": "B12",
            },
            {
                "id": "B13",
            }
        ],
        "crew": [
            {
                "name": "John Doe",
                "occupation": "Pilot"
            },
            {
                "name": "Jane Doe",
                "occupation": "Co-Pilot"
            },
            {
                "name": "John Smith",
                "occupation": "Flight Attendant"
            },
            {
                "name": "Jane Smith",
                "occupation": "Flight Attendant"
            }
        ]
    },
    {
        "id": str(uuid4()),
        "type": "National",
        "departure": airport_list[0],
        "destination": airport_list[2],
        "departure_time": datetime.time(10),
        "departure_date": datetime.date(2022, 11, 20),
        "seats": [
            {
                "id": "A11",
            },
            {
                "id": "A12",
            },
            {
                "id": "A13",
            },
            {
                "id": "B11",
            },
            {
                "id": "B12",
            },
            {
                "id": "B13",
            }
        ],
        "crew": [
            {
                "name": "Augusto Machado",
                "occupation": "Pilot"
            },
            {
                "name": "Maria Silvana",
                "occupation": "Co-Pilot"
            },
            {
                "name": "Cleber Santos",
                "occupation": "Flight Attendant"
            },
            {
                "name": "Larissa Silva",
                "occupation": "Flight Attendant"
            }
        ]
    },
    {
        "id": str(uuid4()),
        "type": "International",
        "departure": airport_list[2],
        "destination": airport_list[0],
        "departure_time": datetime.time(10),
        "departure_date": datetime.date(2022, 11, 20),
        "seats": [
            {
                "id": "A11",
            },
            {
                "id": "A12",
            },
            {
                "id": "A13",
            },
            {
                "id": "B11",
            },
            {
                "id": "B12",
            },
            {
                "id": "B13",
            }
        ],
        "crew": [
            {
                "name": "Augusto Machado",
                "occupation": "Pilot"
            },
            {
                "name": "Maria Silvana",
                "occupation": "Co-Pilot"
            },
            {
                "name": "Cleber Santos",
                "occupation": "Flight Attendant"
            },
            {
                "name": "Larissa Silva",
                "occupation": "Flight Attendant"
            }
        ]
    }
]
