from uuid import uuid4
from model.airport import AirportSchema
from model.city import CitySchema
from model.flight import FlightSchema
from model.seat import SeatSchema
from model.crew import CrewSchema

import datetime

from flask import Flask, request, make_response, jsonify

app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False

city_list = [
    {
        "name": "Guarulhos",
        "state": "São Paulo",
        "country": "Brazil",
    },
    {
        "name": "Los Angeles",
        "state": "California",
        "country": "United States",
    },
    {
        "name": "São Paulo",
        "state": "São Paulo",
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
                "role": "Pilot"
            },
            {
                "name": "Jane Doe",
                "role": "Co-Pilot"
            },
            {
                "name": "John Smith",
                "role": "Flight Attendant"
            },
            {
                "name": "Jane Smith",
                "role": "Flight Attendant"
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
                "role": "Pilot"
            },
            {
                "name": "Maria Silvana",
                "role": "Co-Pilot"
            },
            {
                "name": "Cleber Santos",
                "role": "Flight Attendant"
            },
            {
                "name": "Larissa Silva",
                "role": "Flight Attendant"
            }
        ]
    }
]

# 9506aff3-345e-437d-90ed-99a9e0b1ace0

"""City related routes and methods"""
@app.route('/city', methods=['GET'])
def get_cities():
    return make_response(jsonify(
        cities=CitySchema(many=True).dump(city_list)
    ), 200)

@app.route('/city/add', methods=['POST'])
def add_city():
    city = {
        "name": request.json["name"],
        "state": request.json["state"],
        "country": request.json["country"]
    }

    schema = CitySchema().load(city)

    city_list.append(schema)

    return make_response(jsonify(
        message="City added successfully!",
        city=CitySchema().dump(schema)
    ), 200)


"""Airport related routes and methods"""
@app.route('/airport', methods=['GET'])
def get_airports():
    return make_response(jsonify(
        airports=AirportSchema(many=True).dump(airport_list)
    ), 200)

@app.route('/airport/add', methods=['POST'])
def add_airport():
    # get city that matchs the name from request
    city = [city for city in city_list if city["name"] == request.json["city"]][0]

    airport = {
        "city": city,
        "max_departures": request.json["max_departures"],
        "name": request.json["name"]
    }

    schema = AirportSchema().load(airport)

    airport_list.append(schema)

    return make_response(jsonify(
        message="Airport added successfully!",
        airport=AirportSchema().dump(schema)
    ), 200)
                                     
"""Flight related routes and methods"""
@app.route('/flight', methods=['GET'])
def get_flights():
    return make_response(jsonify(
        flights=FlightSchema(many=True).dump(flight_list)
    ), 200)

@app.route('/flight/destination/<destination>', methods=['GET'])
def get_flight_by_destination(destination: str):
    flight = [flight for flight in flight_list if flight["destination"]["name"] == str(destination)][0]

    return make_response(jsonify(
        flight=FlightSchema().dump(flight)
    ), 200)

@app.route('/flight/departure/<departure>', methods=['GET'])
def get_flight_by_departure(departure: str):
    flight = [flight for flight in flight_list if flight["departure"]["name"] == str(departure)][0]

    return make_response(jsonify(
        flight=FlightSchema().dump(flight)
    ), 200)

app.run(debug=True)