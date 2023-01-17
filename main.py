from model.airport import AirportSchema
from model.city import CitySchema
from model.flight import FlightSchema
from model.seat import SeatSchema
from model.crew import CrewSchema

from db import city_list, airport_list, flight_list

from flask import Flask, request, make_response, jsonify

app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False


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
    try:
        flight = [flight for flight in flight_list if flight["destination"]["city"]["name"] == str(destination)][0]
    except IndexError:
        return make_response(jsonify(
            message="Sorry! There isn't any flight scheduled to this destination!",
            destination=destination
        ), 404)
    
    return make_response(jsonify(
        flight=FlightSchema().dump(flight)
    ), 200)

@app.route('/flight/departure/<departure>', methods=['GET'])
def get_flight_by_departure(departure: str):
    try:
        flight = [flight for flight in flight_list if flight["departure"]["city"]["name"] == str(departure)][0]

    except IndexError:
        return make_response(jsonify(
            message="Sorry! There isn't any flight scheduled from this departure!",
            destination=departure
        ), 404)


    return make_response(jsonify(
        flight=FlightSchema().dump(flight)
    ), 200)

@app.route('/flight/type/<flight_type>', methods=['GET'])
def get_flight_by_type(flight_type: str):
    flight_type = flight_type.capitalize()
    try:
        flight = [flight for flight in flight_list if flight["type"] == str(flight_type)]

    except IndexError:
        return make_response(jsonify(
            message="Sorry! There isn't any flight of this type!",
            destination=flight_type
        ), 404)

    return make_response(jsonify(
        flight=FlightSchema(many=True).dump(flight)
    ), 200)

app.run(debug=True)